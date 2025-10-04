"""資料庫連線管理模組。

包含資料庫引擎、會話管理等功能。
"""

# ===== 標準函式庫 =====
import logging
from typing import Generator

# ===== 第三方套件 =====
from fastapi import HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

# ===== 本地模組 =====
from app.core import settings
from app.database.base import Base
from app.decorators import handle_generic_errors_sync
from app.errors import create_database_error, create_service_unavailable_error
from app.errors.exceptions import APIError

# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


def create_database_engine() -> tuple[Engine, sessionmaker]:
    """建立資料庫引擎和會話工廠。"""
    # 根據環境選擇資料庫
    if settings.testing or settings.app_env == "testing":
        DATABASE_URL = settings.sqlite_connection_string
    else:
        DATABASE_URL = settings.mysql_connection_string

    try:
        # 根據資料庫類型設定不同的引擎參數
        if settings.testing or settings.app_env == "testing":
            # SQLite 配置
            engine = create_engine(
                DATABASE_URL,  # SQLite 連接字串
                echo=False,  # 關閉 SQL 查詢日誌，避免測試輸出過於冗長
                pool_pre_ping=False,  # SQLite 不需要連線檢查
                connect_args={
                    "check_same_thread": False,  # 允許不同執行緒共用同一個資料庫連線，因為 FastAPI 測試時，API 請求和資料庫 session 可能不在同一個執行緒
                },
            )
        else:
            # MySQL 配置
            engine = create_engine(
                DATABASE_URL,  # MySQL 連接字串
                echo=False,  # 關閉 SQL 查詢日誌，避免測試輸出過於冗長
                pool_pre_ping=True,  # 啟用連線檢查，確保連線有效性
                pool_size=10,  # 連線池大小
                max_overflow=10,  # 最大溢出連線數（通常是 pool_size 的 1-2 倍）
                pool_timeout=30,  # 連線超時時間（30秒）
                pool_recycle=3600,  # 連線池回收時間（1小時）
                connect_args={  # pymysql 特定參數
                    "charset": "utf8mb4",  # 使用 utf8mb4 字符集
                },
            )

        # 測試連線
        with engine.connect():
            logger.info("成功建立資料庫引擎，並連結到資料庫")

        # 建立 session 工廠：每次呼叫 SessionLocal()，就生成一個新 Session 實例
        # 確保每個請求，都有一個獨立的資料庫連線，避免共用連線，導致資料庫操作錯亂
        SessionLocal = sessionmaker(
            bind=engine,  # 指定 Session 連線的資料庫引擎（engine）
            autocommit=False,  # 不自動提交，手動呼叫 .commit() 才會儲存資料
            autoflush=False,  # 不自動刷新、不自動將未提交的改動同步到資料庫，需手動呼叫 flush()
        )

        logger.info("成功建立會話工廠")

        return engine, SessionLocal

    except Exception as e:
        raise create_service_unavailable_error(f"資料庫引擎建立失敗：{str(e)}")


# 全域變數，用於儲存引擎和會話工廠
engine: Engine | None = None
SessionLocal: sessionmaker | None = None


def initialize_database() -> None:
    """初始化資料庫引擎和會話工廠。"""
    global engine, SessionLocal

    try:
        engine, SessionLocal = create_database_engine()

        # 在測試環境中創建資料庫表
        if settings.testing or settings.app_env == "testing":
            Base.metadata.create_all(bind=engine)
            logger.info("測試環境資料庫表創建完成")

        logger.info("資料庫初始化完成")
    except Exception as e:
        logger.error(f"資料庫初始化失敗：{str(e)}")
        raise


def get_db() -> Generator[Session, None, None]:
    """資料庫會話依賴注入函式。

    用於 FastAPI 的依賴注入系統，為每個請求提供獨立的資料庫會話。
    使用 yield 確保無論有無錯誤，請求結束後自動關閉 session 連線，避免資源浪費、洩漏。

    Yields:
        Session: SQLAlchemy 資料庫會話實例
    """
    if SessionLocal is None or engine is None:
        raise create_database_error("資料庫尚未初始化")

    logger.info("get_db() called: 建立資料庫連線")
    # db 是實際的 Session 實例，用來進行 add()、query()、commit()、close() 等操作
    db = SessionLocal()
    try:
        # 根據資料庫類型設定不同的參數
        is_sqlite = engine.url.drivername == "sqlite"

        if is_sqlite:
            # SQLite 不需要設定時區和 sql_mode
            # 驗證連線是否有效（輕量級檢查）
            db.execute(text("SELECT 1"))
        else:
            # MySQL 特定設定
            # 設定時區為台灣時間
            db.execute(text("SET time_zone = '+08:00'"))

            # 設定 sql_mode 為嚴格模式（每個連線都會設定）
            db.execute(
                text(
                    "SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'"
                )
            )

            # 驗證連線是否有效（輕量級檢查）
            db.execute(text("SELECT 1"))

        logger.info("get_db() yield: 傳遞資料庫連線給處理函式")
        yield db
    except APIError as e:
        # APIError 類型直接向上傳遞，不要包裝
        logger.error(f"get_db() error: API 錯誤 - {str(e)}")
        db.rollback()
        raise
    except HTTPException as e:
        # HTTPException 類型直接向上傳遞，不要包裝
        logger.error(f"get_db() error: HTTP 錯誤 - {str(e)}")
        db.rollback()
        raise
    except Exception as e:
        # 其他異常包裝成 DatabaseError
        logger.error(f"get_db() error: 資料庫操作錯誤 - {str(e)}")
        db.rollback()
        raise create_database_error(f"資料庫會話建立失敗：{str(e)}")
    finally:
        logger.info("get_db() cleanup: 關閉資料庫連線")
        db.close()


@handle_generic_errors_sync("檢查資料庫連線")
def check_db_connection() -> None:
    """檢查資料庫連線狀態。"""
    if engine is None:
        raise create_database_error("資料庫引擎尚未初始化")

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))  # 執行簡單的查詢來測試連線

"""整合測試資料庫 fixtures。

注意：目前使用 SQLite 臨時檔案資料庫，確保測試隔離，避免記憶體資料庫的會話隔離問題。
生產環境部署前，應切換回 MySQL 進行完整整合測試。
"""

# ===== 標準函式庫 =====
import tempfile

# ===== 第三方套件 =====
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ===== 本地模組 =====
from app.core import settings
from app.database import Base, get_db
from app.factory import create_templates
from app.middleware.error_handler import setup_error_handlers
from app.models import (  # 導入所有模型，因為 SQLAlchemy 需要知道所有表結構才能創建表
    Schedule,
    User,
)
from app.routers import api_router, health_router, main_router


@pytest.fixture(scope="function")
def integration_db_session():
    """建立整合測試專用的資料庫會話實例。"""
    # TODO: 生產環境部署前應切換回 MySQL
    # database_url = settings.mysql_connection_string  # MySQL 連接字串

    # 使用 SQLite 臨時檔案資料庫，所有連線共享同一個檔案，解決會話隔離問題
    # 記憶體資料庫 (sqlite:///:memory:) 每個連線都是新的實例，會導致會話隔離問題
    temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    temp_db.close()
    database_url = f"sqlite:///{temp_db.name}"

    # 建立 SQLite 引擎
    engine = create_engine(
        database_url,
        echo=False,  # 關閉 SQL 查詢日誌，避免測試輸出過於冗長
        pool_pre_ping=False,  # SQLite 不需要連線檢查
        connect_args={
            "check_same_thread": False
        },  # 允許不同執行緒共用同一個資料庫連線，因為 FastAPI 測試時，API 請求和資料庫 session 可能不在同一個執行緒
    )

    # 根據 SQLAlchemy 模型定義，建立對應的資料庫表結構
    Base.metadata.create_all(bind=engine)

    # 建立會話工廠：每次呼叫 TestingSessionLocal()，就生成一個新 Session 實例
    # 確保每個請求，都有一個獨立的資料庫連線，避免共用連線，導致資料庫操作錯亂
    TestingSessionLocal = sessionmaker(
        bind=engine,  # 指定 Session 連線的資料庫引擎（engine）
        autocommit=False,  # 不自動提交，手動呼叫 .commit() 才會儲存資料
        autoflush=False,  # 不自動刷新、不自動將未提交的改動同步到資料庫，需手動呼叫 flush()
    )

    # 建立會話實例
    session = TestingSessionLocal()

    try:
        # TODO: 切換回 MySQL 時需要恢復以下配置
        # session.execute(text("SET time_zone = '+08:00'"))
        # session.execute(
        #     text(
        #         "SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'"
        #     )
        # )
        # session.commit()

        # 將 session 傳遞給測試使用，pytest 會在測試結束後自動執行 finally 清理
        yield session
    except Exception as e:
        # 錯誤處理：會話操作失敗時回滾並重新拋出異常
        session.rollback()
        raise Exception(f"整合測試資料庫會話操作失敗：{str(e)}")
    finally:
        session.rollback()  # 確保任何未提交的更改被回滾
        session.close()  # 確保會話在測試結束後正確關閉，避免資源洩漏


@pytest.fixture(scope="function")
def integration_db_override(integration_db_session):  # 先取得會話實例
    """覆蓋資料庫會話依賴注入函式 get_db。

    讓整合測試使用測試資料庫，而不是實際資料庫。
    """

    def override_get_db():
        """覆蓋 get_db 的函數，直接返回測試會話實例。"""
        try:
            yield integration_db_session
        finally:
            pass

    return override_get_db


@pytest.fixture(scope="function")
def integration_test_client(integration_db_session):
    """建立整合測試專用的 FastAPI 測試客戶端，用於發送 HTTP 請求。"""
    # 創建應用程式實例
    test_app = FastAPI()

    # 設定模板引擎實例
    templates = create_templates(settings)

    # 將 templates 設定到應用程式狀態中，用依賴注入解決循環匯入問題
    test_app.state.templates = templates

    # 設定錯誤處理器
    setup_error_handlers(test_app)

    # 註冊路由，確保測試能訪問完整的 API 功能
    test_app.include_router(main_router)
    test_app.include_router(health_router)
    test_app.include_router(api_router)

    # 覆定義覆蓋函數：存取 integration_db_session
    def override_get_db():
        """覆蓋 get_db 依賴，使用測試專用的資料庫會話實例。"""
        yield integration_db_session

    # 使用 FastAPI 的依賴注入覆蓋機制
    test_app.dependency_overrides[get_db] = override_get_db

    # 創建測試客戶端並提供給測試使用
    with TestClient(test_app) as client:
        yield client

    # 測試結束後，清除依賴注入的覆寫，避免影響其他測試
    test_app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def cleanup_database(integration_db_session):
    """自動清理資料庫，避免測試間互相影響。

    這個 fixture 會自動在每個測試前後清理資料庫，
    確保測試間的資料隔離。
    """
    # 測試前清理：確保資料庫是乾淨的
    integration_db_session.query(Schedule).delete()
    integration_db_session.query(User).delete()
    integration_db_session.commit()

    yield

    # 測試後清理：清理測試產生的資料
    integration_db_session.query(Schedule).delete()
    integration_db_session.query(User).delete()
    integration_db_session.commit()

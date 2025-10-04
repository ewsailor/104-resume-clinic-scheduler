"""單元測試資料庫相關的測試 Fixtures。

提供單元測試用的資料庫會話和相關工具。
使用記憶體資料庫，適合快速單元測試。
"""

# ===== 第三方套件 =====
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# ===== 本地模組 =====
from app.database import Base
from app.models import schedule, user  # noqa: F401


@pytest.fixture
def db_session() -> Session:
    """提供單元測試用的資料庫會話。

    使用記憶體 SQLite 資料庫，適合快速單元測試。
    每個測試都會獲得一個乾淨的資料庫狀態。

    特點：
    - 完全隔離：與真實資料庫無關
    - 自動清理：測試結束後自動銷毀
    - 快速執行：記憶體操作比檔案操作快
    - 無副作用：不會影響其他測試或真實資料

    Returns:
        Session: 測試用的資料庫會話
    """
    # 使用記憶體資料庫進行測試（完全隔離）
    engine = create_engine("sqlite:///:memory:")

    # 建立資料表（每次都是全新的）
    Base.metadata.create_all(bind=engine)

    # 建立會話工廠
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # 建立會話
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        # 清理測試資料（記憶體資料庫會自動清理）
        session.close()

"""資料庫連線模組。

提供資料庫連線相關的基礎設施和配置。
"""

# ===== 本地模組 =====
from .base import Base
from .connection import (
    check_db_connection,
    create_database_engine,
    engine,
    get_db,
    initialize_database,
    SessionLocal,
)

__all__ = [
    # 基礎類別
    "Base",
    # 資料庫連線管理
    "create_database_engine",
    "initialize_database",
    "get_db",
    "check_db_connection",
    # 全域變數
    "engine",
    "SessionLocal",
]

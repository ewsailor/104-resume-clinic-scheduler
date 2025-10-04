"""資料庫模型模組。

提供所有資料庫模型和相關的資料結構定義。
"""

# ===== 本地模組 =====
# 絕對路徑導入（跨模組）
from app.database import Base
from app.enums.models import UserRoleEnum

# 相對路徑導入（同模組）
from .schedule import Schedule
from .user import User

__all__ = [
    # 基礎類別
    "Base",
    # 模型類別
    "Schedule",
    "User",
    # 相關 ENUM
    "UserRoleEnum",
]

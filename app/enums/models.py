"""資料庫模型相關的 ENUM 定義模組。

定義各種資料庫欄位使用的 ENUM 型別，包括使用者角色、時段狀態等。
"""

# ===== 標準函式庫 =====
from enum import Enum


class UserRoleEnum(str, Enum):
    """使用者角色 ENUM"""

    GIVER = "GIVER"
    TAKER = "TAKER"
    SYSTEM = "SYSTEM"


class ScheduleStatusEnum(str, Enum):
    """時段狀態 ENUM"""

    DRAFT = "DRAFT"
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

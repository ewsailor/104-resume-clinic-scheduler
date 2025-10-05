"""Enum 定義模組。

集中管理系統中所有的 Enum 定義，包括：
- 資料庫模型相關的 Enum
- 操作相關的 Enum
"""

# ===== 本地模組 =====
from .models import ScheduleStatusEnum, UserRoleEnum
from .operations import DeletionResult, OperationContext

__all__ = [
    # 模型相關
    "UserRoleEnum",
    "ScheduleStatusEnum",
    # 操作相關
    "OperationContext",
    "DeletionResult",
]

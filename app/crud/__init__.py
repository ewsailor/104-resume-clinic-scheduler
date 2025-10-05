"""CRUD 操作模組。

提供資料庫操作的抽象層，將業務邏輯與資料庫操作分離。

包含：
- 時段 CRUD 操作（schedule_crud）
"""

# ===== 本地模組 =====
# 絕對路徑導入（跨模組）
from app.enums.operations import OperationContext

# 相對路徑導入（同模組）
from .schedule import schedule_crud

__all__ = [
    # CRUD 操作實例
    "schedule_crud",
    # 操作相關 ENUM
    "OperationContext",
]

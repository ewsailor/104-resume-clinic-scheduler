"""服務層模組。

提供業務邏輯處理服務，包括時段管理等。
"""

# ===== 本地模組 =====
from .schedule import schedule_service, ScheduleService

__all__ = [
    # 時段管理服務
    "ScheduleService",
    "schedule_service",
]

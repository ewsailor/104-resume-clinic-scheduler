"""時區處理工具模組。

提供時區轉換和本地時間處理的實用函數。
"""

# ===== 標準函式庫 =====
from datetime import datetime, timedelta, timezone

# 台灣時區 (UTC+8)
TAIWAN_TIMEZONE = timezone(timedelta(hours=8))


def get_local_now_naive() -> datetime:
    """取得當前本地時間（台灣時間），不包含時區資訊。"""
    return datetime.now(TAIWAN_TIMEZONE).replace(tzinfo=None)

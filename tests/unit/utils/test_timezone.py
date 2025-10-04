"""時區處理工具測試（使用 freezegun）。"""

# ===== 第三方套件 =====
# ===== 標準函式庫 =====
from datetime import datetime

from freezegun import freeze_time

# ===== 本地模組 =====
from app.utils.timezone import get_local_now_naive, get_utc_timestamp


# freezegun 邏輯是 UTC = 當地時間 - tz_offset，所以 tz_offset 是 -8 表示 UTC = 當地時間 + 8 小時，即臺灣時間 UTC+8
@freeze_time("2024-01-15 12:30:45", tz_offset=-8)
def test_get_local_now_naive():
    """測試取得台灣時區的本地時間。"""
    # GIVEN：freezegun 模擬當前時間

    # WHEN：呼叫函數取得本地時間
    result = get_local_now_naive()

    # THEN：確認返回正確的時間且無時區資訊
    expected_time = datetime(2024, 1, 15, 12, 30, 45)
    assert result == expected_time

    # 返回的時間物件沒有時區資訊，即 tzinfo 是 None
    assert result.tzinfo is None


@freeze_time("2024-01-15 04:30:45", tz_offset=0)
def test_get_utc_timestamp():
    """測試取得 UTC 時間戳記字串。"""
    # GIVEN：freezegun 模擬當前時間

    # WHEN：呼叫函數取得 UTC 時間戳記字串
    result = get_utc_timestamp()

    # THEN：確認返回 ISO 格式時間戳記，ISO 8601 格式：YYYY-MM-DDTHH:MM:SSZ
    expected_timestamp = "2024-01-15T04:30:45Z"
    assert result == expected_timestamp

    # 字串結尾是 'Z'，表示 UTC 時區
    assert result.endswith("Z")

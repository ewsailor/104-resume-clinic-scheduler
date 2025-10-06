"""整合測試時段 fixtures。

提供整合測試用的時段資料和實例。
"""

# ===== 標準函式庫 =====
from datetime import date, time

# ===== 第三方套件 =====
import pytest

# ===== 本地模組 =====
from app.models import Schedule


@pytest.fixture
def schedule_create_payload():
    """時段建立請求資料。"""
    return {
        "schedules": [
            {
                "giver_id": 1,
                # taker_id 為可選，建立時段時通常為 None（表示可預約）
                # status 由系統自動設定，建立時段時不需要指定
                "date": "2024-12-25",
                "start_time": "09:00:00",
                "end_time": "10:00:00",
                "note": "測試時段",
            }
        ],
        "created_by": 1,
        "created_by_role": "GIVER",
    }


@pytest.fixture
def schedule_in_db(integration_db_session):
    """資料庫中的時段資料，供查詢測試使用。

    避免如果使用 API 建立時段，但遇到錯誤時，
    無法確定是建立時段有問題，還是查詢時段列表有問題。
    """
    test_schedule = Schedule(
        giver_id=1,
        date=date(2024, 12, 25),
        start_time=time(9, 0),
        end_time=time(10, 0),
        note="資料庫中的時段資料",
    )
    integration_db_session.add(test_schedule)
    integration_db_session.commit()
    return test_schedule


@pytest.fixture
def schedule_update_payload():
    """時段更新請求資料。"""
    return {
        "schedule": {
            "note": "更新後的時段",
        },
        "updated_by": 1,
        "updated_by_role": "GIVER",
    }


@pytest.fixture
def schedule_delete_payload():
    """時段刪除請求資料。"""
    return {
        "deleted_by": 1,
        "deleted_by_role": "GIVER",
    }

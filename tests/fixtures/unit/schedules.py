"""單元測試時段相關的測試 Fixtures。

提供單元測試用的時段資料和實例。
"""

# ===== 標準函式庫 =====
from datetime import date, time

# ===== 第三方套件 =====
import pytest
from sqlalchemy.orm import Session

# ===== 本地模組 =====
from app.enums.models import ScheduleStatusEnum
from app.models.schedule import Schedule


# ===== 資料 (Data)：字典格式 =====
@pytest.fixture
def test_giver_schedule_data():
    """提供測試用的 Giver 建立時段資料。

    代表 Giver 提供時段給 Taker 預約的情境。
    """
    return {
        "giver_id": 1,
        "taker_id": None,
        "status": ScheduleStatusEnum.AVAILABLE,
        "date": date(2024, 1, 1),
        "start_time": time(9, 0),
        "end_time": time(10, 0),
        "note": "Giver 提供的可預約時段",
    }


@pytest.fixture
def test_taker_schedule_data():
    """提供測試用的 Taker 建立時段資料。

    代表 Taker 提出時段請求給特定 Giver 回覆的情境。
    """
    return {
        "giver_id": 1,
        "taker_id": 1,
        "status": ScheduleStatusEnum.PENDING,
        "date": date(2024, 1, 2),
        "start_time": time(14, 0),
        "end_time": time(15, 0),
        "note": "Taker 提出的時段請求",
    }


# ===== 實例 (Instance)：實例格式 =====
@pytest.fixture
def test_giver_schedule(db_session: Session) -> Schedule:
    """提供測試用的 Giver 建立時段實例。

    代表 Giver 提供時段給 Taker 預約的情境。
    """
    schedule = Schedule(
        giver_id=1,
        taker_id=None,
        status=ScheduleStatusEnum.AVAILABLE,
        date=date(2024, 1, 1),
        start_time=time(9, 0),
        end_time=time(10, 0),
        note="Giver 提供的可預約時段",
    )

    db_session.add(schedule)
    db_session.commit()
    db_session.refresh(schedule)

    return schedule


@pytest.fixture
def test_taker_schedule(db_session: Session) -> Schedule:
    """提供測試用的 Taker 建立時段實例。

    代表 Taker 提出時段請求給特定 Giver 回覆的情境。
    """
    schedule = Schedule(
        giver_id=1,
        taker_id=1,
        status=ScheduleStatusEnum.PENDING,
        date=date(2024, 1, 2),
        start_time=time(14, 0),
        end_time=time(15, 0),
        note="Taker 提出的時段請求",
    )

    db_session.add(schedule)
    db_session.commit()
    db_session.refresh(schedule)

    return schedule

"""Schedule 模型單元測試。

測試 Schedule 模型的基本功能。
"""

# ===== 標準函式庫 =====
from datetime import date, datetime, time

# ===== 第三方套件 =====
import pytest
from pytest_mock import MockerFixture

# ===== 本地模組 =====
from app.enums.models import ScheduleStatusEnum
from app.models.schedule import Schedule


class TestScheduleModel:
    """Schedule 模型單元測試類別。"""

    def test_schedule_creation(self, test_giver_schedule_data):
        """測試 Schedule 實例創建。"""
        # Given: 使用 test_giver_schedule_data 夾具
        schedule_data = test_giver_schedule_data
        schedule = Schedule(**schedule_data)

        # When: 檢查基本屬性

        # Then: 驗證屬性正確
        # 基本欄位
        assert schedule.giver_id == 1
        assert schedule.taker_id is None
        assert schedule.status == ScheduleStatusEnum.AVAILABLE
        assert schedule.date == date(2024, 1, 1)
        assert schedule.start_time == time(9, 0)
        assert schedule.end_time == time(10, 0)
        assert schedule.note == "Giver 提供的可預約時段"

        # 審計欄位（建立時為 None，需要資料庫觸發）
        assert schedule.created_at is None
        assert schedule.created_by is None
        assert schedule.created_by_role is None
        assert schedule.updated_at is None
        assert schedule.updated_by is None
        assert schedule.updated_by_role is None

        # 系統欄位
        assert schedule.deleted_at is None
        assert schedule.deleted_by is None
        assert schedule.deleted_by_role is None

    # app\models\schedule.py 雖有反向關聯，但單元測試中不需要測試反向關聯，因為涉及資料庫關係，應該在整合測試中測試

    @pytest.mark.parametrize(
        "property_name, initial_value, modified_value, expected_result",
        [
            ("is_active", None, datetime.now(), False),
            ("is_deleted", None, datetime.now(), True),
            (
                "is_available",
                None,
                2,
                False,
            ),  # 代表時段已被 ID=2 的使用者預約，不可預約，不一定要是 2，只要是非 None 的數字即可
        ],
    )
    def test_schedule_properties(
        self,
        test_giver_schedule_data,
        property_name,
        initial_value,
        modified_value,
        expected_result,
    ):
        """測試 Schedule 屬性方法。"""
        # Given: 使用 test_giver_schedule_data 夾具
        schedule_data = test_giver_schedule_data
        schedule = Schedule(**schedule_data)

        # When: 檢查初始狀態並修改
        match property_name:
            case "is_active":
                assert getattr(schedule, property_name) is True
                schedule.deleted_at = modified_value
            case "is_deleted":
                assert getattr(schedule, property_name) is False
                schedule.deleted_at = modified_value
            case "is_available":
                schedule.deleted_at = None  # 確保活躍狀態
                schedule.status = ScheduleStatusEnum.AVAILABLE  # 確保 AVAILABLE 狀態
                assert getattr(schedule, property_name) is True
                schedule.taker_id = modified_value

        # Then: 驗證修改後的行為
        assert getattr(schedule, property_name) == expected_result

    def test_schedule_to_dict(self, test_taker_schedule_data):
        """測試 Schedule to_dict 方法。"""
        # Given: 使用 test_taker_schedule_data 夾具
        schedule_data = test_taker_schedule_data
        schedule = Schedule(**schedule_data)

        # When: 轉換為字典
        result = schedule.to_dict()

        # Then: 驗證字典內容
        assert isinstance(result, dict)

        # 基本欄位
        assert result["id"] is None  # 建立時為 None
        assert result["giver_id"] == 1
        assert result["taker_id"] == 1
        assert result["status"] == ScheduleStatusEnum.PENDING
        assert result["date"] == "2024-01-02"
        assert result["start_time"] == "14:00:00"
        assert result["end_time"] == "15:00:00"
        assert result["note"] == "Taker 提出的時段請求"

        # 審計欄位
        assert result["created_at"] is None  # 建立時為 None
        assert result["created_by"] is None
        assert result["created_by_role"] is None
        assert result["updated_at"] is None  # 建立時為 None
        assert result["updated_by"] is None
        assert result["updated_by_role"] is None

        # 系統欄位
        assert result["deleted_at"] is None
        assert result["deleted_by"] is None
        assert result["deleted_by_role"] is None

        # 關聯欄位（單元測試中為 None）
        assert result["created_by_user"] is None
        assert result["updated_by_user"] is None
        assert result["deleted_by_user"] is None

        # 便利屬性
        assert result["is_active"] is True
        assert result["is_deleted"] is False
        assert result["is_available"] is False

    def test_schedule_to_dict_error_triggered(
        self, test_taker_schedule_data, mocker: MockerFixture
    ):
        """測試 Schedule to_dict 方法是否正確觸發錯誤處理。"""
        # Given: 建立 Schedule 實例
        schedule_data = test_taker_schedule_data
        schedule = Schedule(**schedule_data)

        # When: 模擬 safe_getattr 錯誤
        mock_safe_getattr = mocker.patch('app.models.schedule.safe_getattr')
        mock_safe_getattr.side_effect = Exception("模擬屬性存取錯誤")

        # Then: 驗證錯誤處理被觸發
        result = schedule.to_dict()

        # 驗證錯誤處理被觸發（包含 error 欄位）
        assert "error" in result
        assert result["error"] == "資料序列化時發生錯誤"

        # 驗證返回基本資訊，避免 API 完全失敗
        assert result["id"] is None
        assert result["giver_id"] == 1
        assert result["taker_id"] == 1
        assert result["status"] == ScheduleStatusEnum.PENDING  # 實際的 status 值
        assert result["date"] == "2024-01-02"  # 錯誤處理中的格式化
        assert result["start_time"] == "14:00:00"  # 錯誤處理中的格式化
        assert result["end_time"] == "15:00:00"  # 錯誤處理中的格式化
        assert result["note"] == "Taker 提出的時段請求"  # 實際的 note 值

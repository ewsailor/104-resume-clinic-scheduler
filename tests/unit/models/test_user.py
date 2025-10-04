"""User 模型單元測試。

測試 User 模型的基本屬性、方法和業務邏輯。
專注於單一模型的功能，不涉及資料庫關係。
"""

# ===== 標準函式庫 =====
from datetime import datetime

# ===== 第三方套件 =====
import pytest
from pytest_mock import MockerFixture

# ===== 本地模組 =====
from app.models.user import User


class TestUserModel:
    """User 模型單元測試類別。"""

    def test_user_creation(self, test_user_data):
        """測試 User 實例創建。"""
        # Given: 使用 test_user_data 夾具
        user_data = test_user_data
        user = User(**user_data)

        # When: 測試基本屬性

        # Then: 驗證屬性正確
        # 基本欄位
        assert user.name == "測試使用者"
        assert user.email == "test@example.com"

        # 審計欄位（建立時為 None，需要資料庫觸發）
        assert user.created_at is None
        assert user.updated_at is None

        # 系統欄位
        assert user.deleted_at is None

    # app\models\user.py 雖有反向關聯，但單元測試中不需要測試反向關聯，因為涉及資料庫關係，應該在整合測試中測試

    @pytest.mark.parametrize(
        "property_name, initial_value, modified_value, expected_result",
        [
            ("is_active", None, datetime.now(), False),
            ("is_deleted", None, datetime.now(), True),
        ],
    )
    def test_user_properties(
        self,
        test_user_data,
        property_name,
        initial_value,
        modified_value,
        expected_result,
    ):
        """測試 User 屬性方法。"""
        # Given: 使用 test_user_data 夾具
        user_data = test_user_data
        user = User(**user_data)

        # When: 檢查初始狀態並修改
        match property_name:
            case "is_active":
                assert getattr(user, property_name) is True
                user.deleted_at = modified_value
            case "is_deleted":
                assert getattr(user, property_name) is False
                user.deleted_at = modified_value

        # Then: 驗證修改後的行為
        assert getattr(user, property_name) == expected_result

    def test_user_to_dict(self, test_user_data):
        """測試 User to_dict 方法。"""
        # Given: 使用 test_user_data 夾具
        user_data = test_user_data
        user = User(**user_data)

        # When: 轉換為字典
        result = user.to_dict()

        # Then: 驗證字典內容
        assert isinstance(result, dict)

        # 基本欄位
        assert result["id"] is None  # 建立時為 None
        assert result["name"] == "測試使用者"
        assert result["email"] == "test@example.com"

        # 審計欄位
        assert result["created_at"] is None  # 建立時為 None
        assert result["updated_at"] is None  # 建立時為 None

        # 系統欄位
        assert result["deleted_at"] is None

        # 便利屬性
        assert result["is_active"] is True
        assert result["is_deleted"] is False

    def test_user_to_dict_error_triggered(self, test_user_data, mocker: MockerFixture):
        """測試 User to_dict 方法是否正確觸發錯誤處理。"""
        # Given: 建立 User 實例
        user_data = test_user_data
        user = User(**user_data)

        # When: 模擬 format_datetime 錯誤
        mock_format_datetime = mocker.patch('app.models.user.format_datetime')
        mock_format_datetime.side_effect = Exception("模擬格式化錯誤")

        # Then: 驗證錯誤處理被觸發
        result = user.to_dict()

        # 驗證錯誤處理被觸發（包含 error 欄位）
        assert "error" in result
        assert result["error"] == "資料序列化時發生錯誤"

        # 驗證返回基本資訊，避免 API 完全失敗
        assert result["id"] is None
        assert result["name"] == "測試使用者"  # 實際的 name 值
        assert result["email"] == "test@example.com"  # 實際的 email 值

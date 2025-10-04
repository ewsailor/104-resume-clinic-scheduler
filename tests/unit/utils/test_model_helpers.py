"""模型輔助工具測試。"""

# ===== 標準函式庫 =====
from datetime import date, datetime, time

# ===== 第三方套件 =====
import pytest

# ===== 本地模組 =====
from app.utils.model_helpers import (
    format_datetime,
    safe_getattr,
)


class TestModelHelper:
    """model_helpers 工具函式測試。"""

    # ===== format_datetime =====
    @pytest.mark.parametrize(
        "dt_input, expected_output",
        [
            # datetime 類型測試
            (datetime(2024, 1, 15, 12, 30, 45), "2024-01-15T12:30:45"),
            # date 類型測試
            (date(2024, 1, 15), "2024-01-15"),
            # time 類型測試
            (time(12, 30, 45), "12:30:45"),
        ],
    )
    def test_format_datetime_with_valid_datetime(self, dt_input, expected_output):
        """測試格式化日期時間 - 有效日期時間、日期、時間。

        參數化測試涵蓋三種不同的日期時間類型：
        - datetime: 完整日期時間
        - date: 僅日期
        - time: 僅時間
        """
        # GIVEN：使用參數化的輸入值

        # WHEN：呼叫格式化函數
        result = format_datetime(dt_input)

        # THEN：確認返回正確的 ISO 格式字串
        assert result == expected_output

    def test_format_datetime_with_none(self):
        """測試格式化日期時間 - None 值。"""
        # GIVEN：提供 None 值作為輸入
        dt = None

        # WHEN：呼叫格式化函數
        result = format_datetime(dt)

        # THEN：確認返回 None
        assert result is None

    # ===== safe_getattr =====
    def setup_method(self):
        """每個測試前的初始化，建立測試用的物件實例。"""

        class SampleObject:
            def __init__(self):
                self.name = "test"

        self.sample_object = SampleObject()

    def _create_bad_object(self):
        """建立會拋出例外的測試物件。"""

        class BadObj:
            def __getattribute__(self, name):
                raise Exception("error")

        return BadObj()

    def test_safe_getattr_existing_attribute(self):
        """測試安全取得屬性 - 存在的屬性。"""
        # GIVEN：使用已設定的測試物件

        # WHEN：嘗試取得存在的屬性
        result = safe_getattr(self.sample_object, "name")

        # THEN：確認返回正確的屬性值
        assert result == "test"

    @pytest.mark.parametrize(
        "default_value, expected_result",
        [
            (None, None),  # 無預設值
            ("default", "default"),  # 有預設值
        ],
    )
    def test_safe_getattr_missing_attribute(self, default_value, expected_result):
        """測試安全取得屬性 - 不存在的屬性。

        參數化測試涵蓋兩種情況：
        - 無預設值：返回 None
        - 有預設值：返回提供的預設值
        """
        # GIVEN：建立一個沒有該屬性的物件
        obj = object()

        # WHEN：嘗試取得不存在的屬性
        if default_value is None:
            result = safe_getattr(obj, "missing")
        else:
            result = safe_getattr(obj, "missing", default_value)

        # THEN：確認返回預期的結果
        assert result == expected_result

    @pytest.mark.parametrize(
        "default_value, expected_result",
        [
            (None, None),  # 無預設值
            ("fallback", "fallback"),  # 有預設值
        ],
    )
    def test_safe_getattr_exception_handling(self, default_value, expected_result):
        """測試安全取得屬性 - 例外處理。

        參數化測試涵蓋兩種情況：
        - 無預設值：例外被捕捉並返回 None
        - 有預設值：例外被捕捉並返回預設值
        """
        # GIVEN：建立一個會拋出例外的物件
        bad_obj = self._create_bad_object()

        # WHEN：嘗試取得屬性（會觸發例外）
        if default_value is None:
            result = safe_getattr(bad_obj, "any")
        else:
            result = safe_getattr(bad_obj, "any", default_value)

        # THEN：確認例外被捕捉並返回預期的結果
        assert result == expected_result

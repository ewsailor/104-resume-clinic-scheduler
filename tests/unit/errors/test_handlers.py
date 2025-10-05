"""錯誤處理輔助函式測試模組。

測試是否正確建立錯誤實例，回傳正確的錯誤訊息與型別、正確拋出與捕捉錯誤。
"""

# ===== 第三方套件 =====
import pytest

# ===== 本地模組 =====
from app.errors.exceptions import (  # CRUD 層級; Router 層級; Service 層級; System 層級
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    BusinessLogicError,
    ConflictError,
    DatabaseError,
    ScheduleCannotBeDeletedError,
    ScheduleNotFoundError,
    ScheduleOverlapError,
    ServiceUnavailableError,
    UserNotFoundError,
    ValidationError,
)
from app.errors.handlers import (  # CRUD 層級; Router 層級; Service 層級; System 層級
    create_authentication_error,
    create_authorization_error,
    create_bad_request_error,
    create_business_logic_error,
    create_conflict_error,
    create_database_error,
    create_schedule_cannot_be_deleted_error,
    create_schedule_not_found_error,
    create_schedule_overlap_error,
    create_service_unavailable_error,
    create_user_not_found_error,
    create_validation_error,
    get_deletion_explanation,
)


class TestErrorFactories:
    """錯誤處理輔助函式測試。"""

    @pytest.mark.parametrize(
        "func, exc_class",
        [
            (create_database_error, DatabaseError),
            (create_bad_request_error, BadRequestError),
            (create_authentication_error, AuthenticationError),
            (create_authorization_error, AuthorizationError),
            (create_validation_error, ValidationError),
            (create_business_logic_error, BusinessLogicError),
            (create_conflict_error, ConflictError),
            (create_service_unavailable_error, ServiceUnavailableError),
        ],
    )
    def test_error_factories_return_type_and_message(self, func, exc_class):
        """測試非 ID 相關錯誤處理輔助函式，是否回傳正確型別與錯誤訊息。"""
        # Given: 準備測試參數
        msg = "test message"

        # When: 建立錯誤實例
        error = func(msg)

        # Then: 驗證 error 錯誤型別正確、為 Exception 的實例
        assert isinstance(error, exc_class)
        assert isinstance(error, Exception)

        # Then: 驗證錯誤訊息
        assert str(error) == msg

    @pytest.mark.parametrize(
        "func, exc_class",
        [
            (create_database_error, DatabaseError),
            (create_bad_request_error, BadRequestError),
            (create_authentication_error, AuthenticationError),
            (create_authorization_error, AuthorizationError),
            (create_validation_error, ValidationError),
            (create_business_logic_error, BusinessLogicError),
            (create_conflict_error, ConflictError),
            (create_service_unavailable_error, ServiceUnavailableError),
        ],
    )
    def test_error_factories_raise_behavior(self, func, exc_class):
        """測試非 ID 相關錯誤處理輔助函式，是否正確拋出與捕捉錯誤。"""
        # Given: 準備測試參數
        msg = "raised error"

        # When: 拋出錯誤，並存入 exc_info
        with pytest.raises(exc_class) as exc_info:
            raise func(msg)

        # Then: 驗證錯誤訊息
        assert str(exc_info.value) == msg

    @pytest.mark.parametrize(
        "func, exc_class, param, expected_msg",
        [
            (
                create_schedule_not_found_error,
                ScheduleNotFoundError,
                123,
                "時段不存在: ID=123",
            ),
            (
                create_user_not_found_error,
                UserNotFoundError,
                456,
                "使用者不存在: ID=456",
            ),
            (
                create_schedule_cannot_be_deleted_error,
                ScheduleCannotBeDeletedError,
                789,
                "時段無法刪除: ID=789",
            ),
            (
                create_schedule_overlap_error,
                ScheduleOverlapError,
                "檢測到重疊時段",
                "檢測到重疊時段",
            ),
        ],
    )
    def test_id_error_factories(self, func, exc_class, param, expected_msg):
        """測試 ID 相關錯誤處理輔助函式，是否回傳正確型別與錯誤訊息。"""
        # Given: 準備測試參數

        # When: 建立錯誤實例
        error = func(param)

        # Then: 驗證 error 錯誤型別正確、為 Exception 的實例
        assert isinstance(error, exc_class)
        assert isinstance(error, Exception)

        # Then: 驗證錯誤訊息
        assert str(error) == expected_msg

    @pytest.mark.parametrize(
        "func, exc_class, param, expected_msg",
        [
            (
                create_schedule_not_found_error,
                ScheduleNotFoundError,
                123,
                "時段不存在: ID=123",
            ),
            (
                create_user_not_found_error,
                UserNotFoundError,
                456,
                "使用者不存在: ID=456",
            ),
            (
                create_schedule_cannot_be_deleted_error,
                ScheduleCannotBeDeletedError,
                789,
                "時段無法刪除: ID=789",
            ),
            (
                create_schedule_overlap_error,
                ScheduleOverlapError,
                "檢測到重疊時段",
                "檢測到重疊時段",
            ),
        ],
    )
    def test_id_error_factories_raise_behavior(
        self, func, exc_class, param, expected_msg
    ):
        """測試 ID 相關錯誤處理輔助函式，是否正確拋出與捕捉錯誤。"""
        # Given: 準備測試參數

        # When: 拋出錯誤，並存入 exc_info
        with pytest.raises(exc_class) as exc_info:
            raise func(param)

        # Then: 驗證錯誤訊息
        assert str(exc_info.value) == expected_msg


class TestDeletionExplanation:
    """刪除解釋函數測試。"""

    @pytest.mark.parametrize(
        "status, expected_explanation",
        [
            (
                "ACCEPTED",
                "已接受的時段無法刪除，因為雙方已確認面談時間，刪除會影響約定",
            ),
            (
                "COMPLETED",
                "已完成的時段無法刪除，因為面談已完成，屬於歷史記錄，不應刪除",
            ),
            (None, "時段狀態不允許刪除"),
        ],
    )
    def test_get_deletion_explanation(self, status, expected_explanation):
        """測試刪除解釋函數。"""
        # Given: 準備測試狀態

        # When: 呼叫刪除解釋函數
        result = get_deletion_explanation(status)

        # Then: 驗證回傳的解釋訊息
        assert result == expected_explanation

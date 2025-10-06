"""錯誤類別測試模組。

測試各種自定義錯誤類別的功能。
"""

from fastapi import status

# ===== 第三方套件 =====
import pytest

# ===== 本地模組 =====
from app.errors.exceptions import (  # 基礎錯誤類別; CRUD 層級錯誤; Router 層級錯誤; Service 層級錯誤; System 層級錯誤
    APIError,
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


# ===== APIError 基礎類別測試 =====
class TestAPIError:
    """APIError 基礎類別測試。"""

    @pytest.mark.parametrize(
        "message,error_code,status_code,details,expected_details",
        [
            # 基本測試
            ("測試錯誤", "TEST_ERROR", status.HTTP_400_BAD_REQUEST, None, {}),
            # 邊界測試：空詳細資訊
            ("測試錯誤", "TEST_ERROR", status.HTTP_400_BAD_REQUEST, {}, {}),
            # 自定義狀態碼測試
            ("測試錯誤", "TEST_ERROR", status.HTTP_500_INTERNAL_SERVER_ERROR, None, {}),
            # 帶詳細資訊測試
            (
                "測試錯誤",
                "TEST_ERROR",
                status.HTTP_400_BAD_REQUEST,
                {"code": 123, "msg": "error"},
                {"code": 123, "msg": "error"},
            ),
        ],
    )
    def test_api_error_creation(
        self,
        message: str,
        error_code: str,
        status_code: int,
        details: dict | None,
        expected_details: dict,
    ) -> None:
        """測試 APIError 類別的正確建立與屬性設定。"""
        # Given: 準備測試參數，由參數化測試提供

        # When: 建立 APIError 實例
        error = APIError(
            message=message,
            error_code=error_code,
            status_code=status_code,
            details=details,
        )

        # Then: 驗證資料完整性
        assert error.message == message
        assert error.error_code == error_code
        assert error.status_code == status_code
        assert error.details == expected_details
        assert str(error) == message

    def test_api_error_inheritance(self):
        """測試 APIError 繼承關係。"""
        # Given: 準備測試資料
        message = "測試錯誤"
        error_code = "TEST_ERROR"

        # When: 建立 APIError 實例
        error = APIError(message, error_code)

        # Then: 驗證 APIError 正確繼承自 Exception，可被 except Exception 捕獲
        assert isinstance(error, Exception)


# ===== 錯誤層級測試 =====
class TestErrorHierarchy:
    """錯誤層級測試。"""

    @pytest.mark.parametrize(
        "error_class,args,expected_error_code,expected_status_code",
        [
            # CRUD 層級錯誤
            (
                DatabaseError,
                ("test",),
                "CRUD_DATABASE_ERROR",
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            ),
            # Router 層級錯誤
            (
                BadRequestError,
                ("test",),
                "ROUTER_BAD_REQUEST",
                status.HTTP_400_BAD_REQUEST,
            ),
            (
                AuthenticationError,
                ("test",),
                "ROUTER_AUTHENTICATION_ERROR",
                status.HTTP_401_UNAUTHORIZED,
            ),
            (
                AuthorizationError,
                ("test",),
                "ROUTER_AUTHORIZATION_ERROR",
                status.HTTP_403_FORBIDDEN,
            ),
            (
                ValidationError,
                ("test",),
                "ROUTER_VALIDATION_ERROR",
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            ),
            # Service 層級錯誤
            (
                BusinessLogicError,
                ("test",),
                "SERVICE_BUSINESS_LOGIC_ERROR",
                status.HTTP_400_BAD_REQUEST,
            ),
            (
                ScheduleNotFoundError,
                (1,),
                "SERVICE_SCHEDULE_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
            ),
            (
                UserNotFoundError,
                (1,),
                "SERVICE_USER_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
            ),
            (ConflictError, ("test",), "SERVICE_CONFLICT", status.HTTP_409_CONFLICT),
            (
                ScheduleCannotBeDeletedError,
                (1,),
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                status.HTTP_409_CONFLICT,
            ),
            (
                ScheduleOverlapError,
                ("test",),
                "SERVICE_SCHEDULE_OVERLAP",
                status.HTTP_409_CONFLICT,
            ),
            # System 層級錯誤
            (
                ServiceUnavailableError,
                ("test",),
                "SERVICE_UNAVAILABLE",
                status.HTTP_503_SERVICE_UNAVAILABLE,
            ),
        ],
    )
    def test_error_inheritance_and_attributes(
        self, error_class, args, expected_error_code, expected_status_code
    ):
        """測試錯誤繼承關係、錯誤代碼和狀態碼。"""
        # Given: 準備測試資料（由參數化測試提供）

        # When: 建立錯誤實例
        error = error_class(*args)

        # Then: 驗證繼承關係和固定屬性
        assert isinstance(
            error, APIError
        )  # 驗證繼承自 APIError，確保所有錯誤有相同的錯誤屬性（message, error_code, status_code, details）
        assert isinstance(
            error, Exception
        )  # 驗證繼承自 Exception，確保所有錯誤可被 Python 的異常處理機制正確捕獲
        assert error.error_code == expected_error_code
        assert error.status_code == expected_status_code


# ===== 統一的錯誤類別測試 =====
class TestExceptionCreation:
    """統一測試所有錯誤類別的建立功能。"""

    @pytest.mark.parametrize(
        "error_class,args,expected_message,expected_error_code,expected_status_code,expected_details",
        [
            # CRUD 層級錯誤
            (
                DatabaseError,
                ("資料庫操作失敗", None),
                "資料庫操作失敗",
                "CRUD_DATABASE_ERROR",
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                {},
            ),
            (
                DatabaseError,
                ("資料庫連線超時", {}),
                "資料庫連線超時",
                "CRUD_DATABASE_ERROR",
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                {},
            ),
            (
                DatabaseError,
                ("資料庫操作失敗", {"operation": "INSERT"}),
                "資料庫操作失敗",
                "CRUD_DATABASE_ERROR",
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                {"operation": "INSERT"},
            ),
            # Router 層級錯誤
            (
                BadRequestError,
                ("請求格式錯誤", None),
                "請求格式錯誤",
                "ROUTER_BAD_REQUEST",
                status.HTTP_400_BAD_REQUEST,
                {},
            ),
            (
                BadRequestError,
                ("請求格式錯誤", {}),
                "請求格式錯誤",
                "ROUTER_BAD_REQUEST",
                status.HTTP_400_BAD_REQUEST,
                {},
            ),
            (
                BadRequestError,
                ("請求格式錯誤", {"field": "request_body", "error": "格式不正確"}),
                "請求格式錯誤",
                "ROUTER_BAD_REQUEST",
                status.HTTP_400_BAD_REQUEST,
                {"field": "request_body", "error": "格式不正確"},
            ),
            (
                AuthenticationError,
                ("認證失敗", None),
                "認證失敗",
                "ROUTER_AUTHENTICATION_ERROR",
                status.HTTP_401_UNAUTHORIZED,
                {},
            ),
            (
                AuthenticationError,
                ("認證失敗", {}),
                "認證失敗",
                "ROUTER_AUTHENTICATION_ERROR",
                status.HTTP_401_UNAUTHORIZED,
                {},
            ),
            (
                AuthenticationError,
                ("認證失敗", {"token": "invalid"}),
                "認證失敗",
                "ROUTER_AUTHENTICATION_ERROR",
                status.HTTP_401_UNAUTHORIZED,
                {"token": "invalid"},
            ),
            (
                AuthorizationError,
                ("權限不足", None),
                "權限不足",
                "ROUTER_AUTHORIZATION_ERROR",
                status.HTTP_403_FORBIDDEN,
                {},
            ),
            (
                AuthorizationError,
                ("權限不足", {}),
                "權限不足",
                "ROUTER_AUTHORIZATION_ERROR",
                status.HTTP_403_FORBIDDEN,
                {},
            ),
            (
                AuthorizationError,
                ("權限不足", {"resource": "admin"}),
                "權限不足",
                "ROUTER_AUTHORIZATION_ERROR",
                status.HTTP_403_FORBIDDEN,
                {"resource": "admin"},
            ),
            (
                ValidationError,
                ("驗證失敗", None),
                "驗證失敗",
                "ROUTER_VALIDATION_ERROR",
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {},
            ),
            (
                ValidationError,
                ("驗證失敗", {}),
                "驗證失敗",
                "ROUTER_VALIDATION_ERROR",
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {},
            ),
            (
                ValidationError,
                ("驗證失敗", {"field": "email", "error": "格式不正確"}),
                "驗證失敗",
                "ROUTER_VALIDATION_ERROR",
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {"field": "email", "error": "格式不正確"},
            ),
            # Service 層級錯誤
            (
                BusinessLogicError,
                ("業務邏輯錯誤", None),
                "業務邏輯錯誤",
                "SERVICE_BUSINESS_LOGIC_ERROR",
                status.HTTP_400_BAD_REQUEST,
                {},
            ),
            (
                BusinessLogicError,
                ("業務邏輯錯誤", {}),
                "業務邏輯錯誤",
                "SERVICE_BUSINESS_LOGIC_ERROR",
                status.HTTP_400_BAD_REQUEST,
                {},
            ),
            (
                BusinessLogicError,
                ("業務邏輯錯誤", {"operation": "create", "reason": "conflict"}),
                "業務邏輯錯誤",
                "SERVICE_BUSINESS_LOGIC_ERROR",
                status.HTTP_400_BAD_REQUEST,
                {"operation": "create", "reason": "conflict"},
            ),
            (
                ScheduleNotFoundError,
                (123, None),
                "時段不存在: ID=123",
                "SERVICE_SCHEDULE_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {},
            ),
            (
                ScheduleNotFoundError,
                ("abc123", None),
                "時段不存在: ID=abc123",
                "SERVICE_SCHEDULE_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {},
            ),
            (
                ScheduleNotFoundError,
                (123, {}),
                "時段不存在: ID=123",
                "SERVICE_SCHEDULE_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {},
            ),
            (
                ScheduleNotFoundError,
                (123, {"search_criteria": "date=2024-01-01"}),
                "時段不存在: ID=123",
                "SERVICE_SCHEDULE_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {"search_criteria": "date=2024-01-01"},
            ),
            (
                UserNotFoundError,
                (456, None),
                "使用者不存在: ID=456",
                "SERVICE_USER_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {},
            ),
            (
                UserNotFoundError,
                ("user123", None),
                "使用者不存在: ID=user123",
                "SERVICE_USER_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {},
            ),
            (
                UserNotFoundError,
                (456, {}),
                "使用者不存在: ID=456",
                "SERVICE_USER_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {},
            ),
            (
                UserNotFoundError,
                (456, {"email": "test@example.com"}),
                "使用者不存在: ID=456",
                "SERVICE_USER_NOT_FOUND",
                status.HTTP_404_NOT_FOUND,
                {"email": "test@example.com"},
            ),
            (
                ConflictError,
                ("資源衝突", None),
                "資源衝突",
                "SERVICE_CONFLICT",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ConflictError,
                ("資源衝突", {}),
                "資源衝突",
                "SERVICE_CONFLICT",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ConflictError,
                (
                    "資源衝突",
                    {
                        "conflicting_field": "email",
                        "existing_value": "test@example.com",
                    },
                ),
                "資源衝突",
                "SERVICE_CONFLICT",
                status.HTTP_409_CONFLICT,
                {"conflicting_field": "email", "existing_value": "test@example.com"},
            ),
            (
                ScheduleCannotBeDeletedError,
                (123, None),
                "時段無法刪除: ID=123",
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ScheduleCannotBeDeletedError,
                ("abc123", None),
                "時段無法刪除: ID=abc123",
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ScheduleCannotBeDeletedError,
                (123, {}),
                "時段無法刪除: ID=123",
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ScheduleCannotBeDeletedError,
                (123, {"reason": "schedule_already_accepted"}),
                "時段無法刪除: ID=123",
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                status.HTTP_409_CONFLICT,
                {"reason": "schedule_already_accepted"},
            ),
            (
                ScheduleOverlapError,
                ("時段時間重疊", None),
                "時段時間重疊",
                "SERVICE_SCHEDULE_OVERLAP",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ScheduleOverlapError,
                ("時段時間重疊", {}),
                "時段時間重疊",
                "SERVICE_SCHEDULE_OVERLAP",
                status.HTTP_409_CONFLICT,
                {},
            ),
            (
                ScheduleOverlapError,
                (
                    "時段時間重疊",
                    {
                        "existing_schedule_id": 123,
                        "overlap_start": "09:00",
                        "overlap_end": "10:00",
                    },
                ),
                "時段時間重疊",
                "SERVICE_SCHEDULE_OVERLAP",
                status.HTTP_409_CONFLICT,
                {
                    "existing_schedule_id": 123,
                    "overlap_start": "09:00",
                    "overlap_end": "10:00",
                },
            ),
            # System 層級錯誤
            (
                ServiceUnavailableError,
                ("服務暫時不可用", None),
                "服務暫時不可用",
                "SERVICE_UNAVAILABLE",
                status.HTTP_503_SERVICE_UNAVAILABLE,
                {},
            ),
            (
                ServiceUnavailableError,
                ("服務暫時不可用", {}),
                "服務暫時不可用",
                "SERVICE_UNAVAILABLE",
                status.HTTP_503_SERVICE_UNAVAILABLE,
                {},
            ),
            (
                ServiceUnavailableError,
                ("維護中", {"duration": "2小時"}),
                "維護中",
                "SERVICE_UNAVAILABLE",
                status.HTTP_503_SERVICE_UNAVAILABLE,
                {"duration": "2小時"},
            ),
        ],
    )
    def test_error_creation(
        self,
        error_class,
        args,
        expected_message: str,
        expected_error_code: str,
        expected_status_code: int,
        expected_details: dict,
    ) -> None:
        """測試錯誤類別建立功能 - 統一參數化測試。"""
        # Given: 錯誤類別和參數，由參數化測試提供

        # When: 建立錯誤實例
        error = error_class(*args)

        # Then: 驗證錯誤屬性
        assert error.message == expected_message
        assert error.error_code == expected_error_code
        assert error.status_code == expected_status_code
        assert error.details == expected_details
        assert str(error) == expected_message

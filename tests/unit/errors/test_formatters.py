"""錯誤格式化測試模組。

測試錯誤格式化功能。
"""

# ===== 標準函式庫 =====
from unittest.mock import patch

# ===== 第三方套件 =====
from fastapi import HTTPException
import pytest

# ===== 本地模組 =====
from app.errors.exceptions import (  # CRUD 層級; Router 層級; Service 層級; System 層級
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
from app.errors.formatters import format_error_response


class TestFormatErrorResponse:
    """format_error_response 函數測試。"""

    @pytest.mark.parametrize(
        "error_factory,expected_message,expected_status_code,expected_code,expected_details",
        [
            # ===== APIError 基礎類別測試 =====
            # 基本測試
            (
                lambda: APIError("基礎錯誤", "TEST_ERROR"),
                "基礎錯誤",
                400,
                "TEST_ERROR",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: APIError("基礎錯誤", "TEST_ERROR", 400, {}),
                "基礎錯誤",
                400,
                "TEST_ERROR",
                {},
            ),
            # 自定義狀態碼測試
            (
                lambda: APIError("基礎錯誤", "TEST_ERROR", 500),
                "基礎錯誤",
                500,
                "TEST_ERROR",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: APIError("基礎錯誤", "TEST_ERROR", 400, {"test": "value"}),
                "基礎錯誤",
                400,
                "TEST_ERROR",
                {"test": "value"},
            ),
            # ===== CRUD 層級錯誤測試 =====
            # DatabaseError 測試
            # 基本測試
            (
                lambda: DatabaseError("資料庫錯誤"),
                "資料庫錯誤",
                500,
                "CRUD_DATABASE_ERROR",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: DatabaseError("資料庫錯誤", {}),
                "資料庫錯誤",
                500,
                "CRUD_DATABASE_ERROR",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: DatabaseError("資料庫錯誤", {"table": "users"}),
                "資料庫錯誤",
                500,
                "CRUD_DATABASE_ERROR",
                {"table": "users"},
            ),
            # ===== Router 層級錯誤測試 =====
            # BadRequestError 測試
            # 基本測試
            (
                lambda: BadRequestError("請求錯誤"),
                "請求錯誤",
                400,
                "ROUTER_BAD_REQUEST",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: BadRequestError("請求錯誤", {}),
                "請求錯誤",
                400,
                "ROUTER_BAD_REQUEST",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: BadRequestError("請求錯誤", {"field": "body"}),
                "請求錯誤",
                400,
                "ROUTER_BAD_REQUEST",
                {"field": "body"},
            ),
            # AuthenticationError 測試
            # 基本測試
            (
                lambda: AuthenticationError("認證錯誤"),
                "認證錯誤",
                401,
                "ROUTER_AUTHENTICATION_ERROR",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: AuthenticationError("認證錯誤", {}),
                "認證錯誤",
                401,
                "ROUTER_AUTHENTICATION_ERROR",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: AuthenticationError("認證錯誤", {"token": "invalid"}),
                "認證錯誤",
                401,
                "ROUTER_AUTHENTICATION_ERROR",
                {"token": "invalid"},
            ),
            # AuthorizationError 測試
            # 基本測試
            (
                lambda: AuthorizationError("權限錯誤"),
                "權限錯誤",
                403,
                "ROUTER_AUTHORIZATION_ERROR",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: AuthorizationError("權限錯誤", {}),
                "權限錯誤",
                403,
                "ROUTER_AUTHORIZATION_ERROR",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: AuthorizationError("權限錯誤", {"resource": "admin"}),
                "權限錯誤",
                403,
                "ROUTER_AUTHORIZATION_ERROR",
                {"resource": "admin"},
            ),
            # ValidationError 測試
            # 基本測試
            (
                lambda: ValidationError("驗證錯誤"),
                "驗證錯誤",
                422,
                "ROUTER_VALIDATION_ERROR",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: ValidationError("驗證錯誤", {}),
                "驗證錯誤",
                422,
                "ROUTER_VALIDATION_ERROR",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: ValidationError("驗證錯誤", {"field": "email"}),
                "驗證錯誤",
                422,
                "ROUTER_VALIDATION_ERROR",
                {"field": "email"},
            ),
            # ===== Service 層級錯誤測試 =====
            # BusinessLogicError 測試
            # 基本測試
            (
                lambda: BusinessLogicError("業務邏輯錯誤"),
                "業務邏輯錯誤",
                400,
                "SERVICE_BUSINESS_LOGIC_ERROR",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: BusinessLogicError("業務邏輯錯誤", {}),
                "業務邏輯錯誤",
                400,
                "SERVICE_BUSINESS_LOGIC_ERROR",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: BusinessLogicError("業務邏輯錯誤", {"operation": "create"}),
                "業務邏輯錯誤",
                400,
                "SERVICE_BUSINESS_LOGIC_ERROR",
                {"operation": "create"},
            ),
            # ScheduleNotFoundError 測試
            # 基本測試
            (
                lambda: ScheduleNotFoundError(123),
                "時段不存在: ID=123",
                404,
                "SERVICE_SCHEDULE_NOT_FOUND",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: ScheduleNotFoundError(123, {}),
                "時段不存在: ID=123",
                404,
                "SERVICE_SCHEDULE_NOT_FOUND",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: ScheduleNotFoundError(123, {"search": "date=2024-01-01"}),
                "時段不存在: ID=123",
                404,
                "SERVICE_SCHEDULE_NOT_FOUND",
                {"search": "date=2024-01-01"},
            ),
            # UserNotFoundError 測試
            # 基本測試
            (
                lambda: UserNotFoundError(456),
                "使用者不存在: ID=456",
                404,
                "SERVICE_USER_NOT_FOUND",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: UserNotFoundError(456, {}),
                "使用者不存在: ID=456",
                404,
                "SERVICE_USER_NOT_FOUND",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: UserNotFoundError(456, {"email": "test@example.com"}),
                "使用者不存在: ID=456",
                404,
                "SERVICE_USER_NOT_FOUND",
                {"email": "test@example.com"},
            ),
            # ConflictError 測試
            # 基本測試
            (
                lambda: ConflictError("衝突錯誤"),
                "衝突錯誤",
                409,
                "SERVICE_CONFLICT",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: ConflictError("衝突錯誤", {}),
                "衝突錯誤",
                409,
                "SERVICE_CONFLICT",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: ConflictError("衝突錯誤", {"field": "email"}),
                "衝突錯誤",
                409,
                "SERVICE_CONFLICT",
                {"field": "email"},
            ),
            # ScheduleCannotBeDeletedError 測試
            # 基本測試
            (
                lambda: ScheduleCannotBeDeletedError(123),
                "時段無法刪除: ID=123",
                409,
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: ScheduleCannotBeDeletedError(123, {}),
                "時段無法刪除: ID=123",
                409,
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: ScheduleCannotBeDeletedError(123, {"reason": "accepted"}),
                "時段無法刪除: ID=123",
                409,
                "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                {"reason": "accepted"},
            ),
            # ScheduleOverlapError 測試
            # 基本測試
            (
                lambda: ScheduleOverlapError("時段重疊錯誤"),
                "時段重疊錯誤",
                409,
                "SERVICE_SCHEDULE_OVERLAP",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: ScheduleOverlapError("時段重疊錯誤", {}),
                "時段重疊錯誤",
                409,
                "SERVICE_SCHEDULE_OVERLAP",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: ScheduleOverlapError("時段重疊錯誤", {"existing": 123}),
                "時段重疊錯誤",
                409,
                "SERVICE_SCHEDULE_OVERLAP",
                {"existing": 123},
            ),
            # ===== System 層級錯誤測試 =====
            # ServiceUnavailableError 測試
            # 基本測試
            (
                lambda: ServiceUnavailableError("服務錯誤"),
                "服務錯誤",
                503,
                "SERVICE_UNAVAILABLE",
                {},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: ServiceUnavailableError("服務錯誤", {}),
                "服務錯誤",
                503,
                "SERVICE_UNAVAILABLE",
                {},
            ),
            # 帶詳細資訊測試
            (
                lambda: ServiceUnavailableError("服務錯誤", {"duration": "2小時"}),
                "服務錯誤",
                503,
                "SERVICE_UNAVAILABLE",
                {"duration": "2小時"},
            ),
        ],
    )
    @patch('app.errors.formatters.get_utc_timestamp')
    def test_format_api_error_response(
        self,
        mock_timestamp,
        error_factory,
        expected_message,
        expected_status_code,
        expected_code,
        expected_details,
    ):
        """測試格式化 APIError 類型錯誤和回應結構。"""
        # Given: 準備測試環境和預期結果
        mock_timestamp.return_value = "2024-01-01T00:00:00Z"
        expected = {
            "error": {
                "message": expected_message,
                "status_code": expected_status_code,
                "code": expected_code,
                "timestamp": "2024-01-01T00:00:00Z",
                "details": expected_details,
            }
        }
        required_fields = ["message", "status_code", "code", "timestamp", "details"]

        # When: 建立錯誤並格式化
        error = error_factory()
        result = format_error_response(error)

        # Then: 驗證格式化結果
        assert result == expected

        # 驗證回應結構
        assert "error" in result
        error_obj = result["error"]

        # 驗證必要欄位存在
        for field in required_fields:
            assert field in error_obj

        # 驗證欄位類型
        assert isinstance(error_obj["message"], str)
        assert isinstance(error_obj["status_code"], int)
        assert isinstance(error_obj["code"], str)
        assert isinstance(error_obj["timestamp"], str)
        assert isinstance(error_obj["details"], dict)

    @pytest.mark.parametrize(
        "error_factory,expected_message,expected_status_code,expected_code,expected_details",
        [
            # ===== 4xx 客戶端錯誤 =====
            # 400 Bad Request
            (
                lambda: HTTPException(status_code=400, detail="Bad Request"),
                "Bad Request",
                400,
                "HTTP_400",
                {"detail": "Bad Request"},
            ),
            # 邊界測試：空 detail 屬性
            (
                lambda: HTTPException(status_code=400, detail=''),
                "請求錯誤",
                400,
                "HTTP_400",
                {},
            ),
            # 401 Unauthorized
            (
                lambda: HTTPException(status_code=401, detail="Unauthorized"),
                "Unauthorized",
                401,
                "HTTP_401",
                {"detail": "Unauthorized"},
            ),
            # 403 Forbidden
            (
                lambda: HTTPException(status_code=403, detail="Forbidden"),
                "Forbidden",
                403,
                "HTTP_403",
                {"detail": "Forbidden"},
            ),
            # 404 Not Found
            (
                lambda: HTTPException(status_code=404, detail="Not Found"),
                "Not Found",
                404,
                "HTTP_404",
                {"detail": "Not Found"},
            ),
            # 405 Method Not Allowed
            (
                lambda: HTTPException(status_code=405, detail="Method Not Allowed"),
                "Method Not Allowed",
                405,
                "HTTP_405",
                {"detail": "Method Not Allowed"},
            ),
            # 409 Conflict
            (
                lambda: HTTPException(status_code=409, detail="Conflict"),
                "Conflict",
                409,
                "HTTP_409",
                {"detail": "Conflict"},
            ),
            # 422 Unprocessable Entity
            (
                lambda: HTTPException(status_code=422, detail="Validation Error"),
                "Validation Error",
                422,
                "HTTP_422",
                {"detail": "Validation Error"},
            ),
            # ===== 5xx 伺服器錯誤 =====
            # 500 Internal Server Error
            (
                lambda: HTTPException(status_code=500, detail="Internal Server Error"),
                "Internal Server Error",
                500,
                "HTTP_500",
                {"detail": "Internal Server Error"},
            ),
            # 502 Bad Gateway
            (
                lambda: HTTPException(status_code=502, detail="Bad Gateway"),
                "Bad Gateway",
                502,
                "HTTP_502",
                {"detail": "Bad Gateway"},
            ),
            # 503 Service Unavailable
            (
                lambda: HTTPException(status_code=503, detail="Service Unavailable"),
                "Service Unavailable",
                503,
                "HTTP_503",
                {"detail": "Service Unavailable"},
            ),
            # 504 Gateway Timeout
            (
                lambda: HTTPException(status_code=504, detail="Gateway Timeout"),
                "Gateway Timeout",
                504,
                "HTTP_504",
                {"detail": "Gateway Timeout"},
            ),
        ],
    )
    @patch('app.errors.formatters.get_utc_timestamp')
    def test_format_http_exception_response(
        self,
        mock_timestamp,
        error_factory,
        expected_message,
        expected_status_code,
        expected_code,
        expected_details,
    ):
        """測試格式化 HTTPException 類型錯誤和回應結構。"""
        # Given: 準備測試環境和預期結果
        mock_timestamp.return_value = "2024-01-01T00:00:00Z"
        expected = {
            "error": {
                "message": expected_message,
                "status_code": expected_status_code,
                "code": expected_code,
                "timestamp": "2024-01-01T00:00:00Z",
                "details": expected_details,
            }
        }
        required_fields = ["message", "status_code", "code", "timestamp", "details"]

        # When: 建立錯誤並格式化
        error = error_factory()
        result = format_error_response(error)

        # Then: 驗證格式化結果
        assert result == expected

        # 驗證回應結構
        assert "error" in result
        error_obj = result["error"]

        # 驗證必要欄位存在
        for field in required_fields:
            assert field in error_obj

        # 驗證欄位類型
        assert isinstance(error_obj["message"], str)
        assert isinstance(error_obj["status_code"], int)
        assert isinstance(error_obj["code"], str)
        assert isinstance(error_obj["timestamp"], str)
        assert isinstance(error_obj["details"], dict)

    @pytest.mark.parametrize(
        "error_factory,expected_message,expected_status_code,expected_code,expected_details",
        [
            # 基本測試
            (
                lambda: ValueError("一般錯誤"),
                "一般錯誤",
                500,
                "INTERNAL_ERROR",
                {"error": "一般錯誤"},
            ),
            # 邊界測試：空詳細資訊
            (
                lambda: Exception(),
                "",
                500,
                "INTERNAL_ERROR",
                {"error": ""},
            ),
            # 帶詳細資訊測試
            (
                lambda: Exception("一般錯誤", {"error": "一般錯誤"}),
                "('一般錯誤', {'error': '一般錯誤'})",
                500,
                "INTERNAL_ERROR",
                {"error": "('一般錯誤', {'error': '一般錯誤'})"},
            ),
            # TypeError 測試
            (
                lambda: TypeError("類型錯誤"),
                "類型錯誤",
                500,
                "INTERNAL_ERROR",
                {"error": "類型錯誤"},
            ),
            # AttributeError 測試
            (
                lambda: AttributeError("屬性錯誤"),
                "屬性錯誤",
                500,
                "INTERNAL_ERROR",
                {"error": "屬性錯誤"},
            ),
            # RuntimeError 測試
            (
                lambda: RuntimeError("運行時錯誤"),
                "運行時錯誤",
                500,
                "INTERNAL_ERROR",
                {"error": "運行時錯誤"},
            ),
            # KeyError 測試
            (
                lambda: KeyError("missing_key"),
                "'missing_key'",
                500,
                "INTERNAL_ERROR",
                {"error": "'missing_key'"},
            ),
            # IndexError 測試
            (
                lambda: IndexError("list index out of range"),
                "list index out of range",
                500,
                "INTERNAL_ERROR",
                {"error": "list index out of range"},
            ),
            # FileNotFoundError 測試
            (
                lambda: FileNotFoundError("No such file or directory: 'test.txt'"),
                "No such file or directory: 'test.txt'",
                500,
                "INTERNAL_ERROR",
                {"error": "No such file or directory: 'test.txt'"},
            ),
            # PermissionError 測試
            (
                lambda: PermissionError("Permission denied: 'config.json'"),
                "Permission denied: 'config.json'",
                500,
                "INTERNAL_ERROR",
                {"error": "Permission denied: 'config.json'"},
            ),
            # ZeroDivisionError 測試
            (
                lambda: ZeroDivisionError("division by zero"),
                "division by zero",
                500,
                "INTERNAL_ERROR",
                {"error": "division by zero"},
            ),
        ],
    )
    @patch('app.errors.formatters.get_utc_timestamp')
    def test_format_generic_error_response(
        self,
        mock_timestamp,
        error_factory,
        expected_message,
        expected_status_code,
        expected_code,
        expected_details,
    ):
        """測試格式化一般異常類型和回應結構。"""
        # Given: 準備測試環境和預期結果
        mock_timestamp.return_value = "2024-01-01T00:00:00Z"
        expected = {
            "error": {
                "message": expected_message,
                "status_code": expected_status_code,
                "code": expected_code,
                "timestamp": "2024-01-01T00:00:00Z",
                "details": expected_details,
            }
        }
        required_fields = ["message", "status_code", "code", "timestamp", "details"]

        # When: 建立錯誤並格式化
        error = error_factory()
        result = format_error_response(error)

        # Then: 驗證格式化結果
        assert result == expected

        # 驗證回應結構
        assert "error" in result
        error_obj = result["error"]

        # 驗證必要欄位存在
        for field in required_fields:
            assert field in error_obj

        # 驗證欄位類型
        assert isinstance(error_obj["message"], str)
        assert isinstance(error_obj["status_code"], int)
        assert isinstance(error_obj["code"], str)
        assert isinstance(error_obj["timestamp"], str)
        assert isinstance(error_obj["details"], dict)

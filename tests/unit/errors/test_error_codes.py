"""錯誤代碼測試模組。

測試各種錯誤代碼常數。
"""

# ===== 第三方套件 =====
import pytest

# ===== 本地模組 =====
from app.errors.error_codes.cors import CORSErrorCode
from app.errors.error_codes.crud import CRUDErrorCode
from app.errors.error_codes.router import RouterErrorCode
from app.errors.error_codes.service import ServiceErrorCode
from app.errors.error_codes.system import SystemErrorCode
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


class TestErrorCodes:
    """錯誤代碼測試。"""

    def _get_error_codes(self, error_class):
        """取得錯誤代碼類別中的所有錯誤代碼字串。

        Args:
            error_class: 錯誤代碼類別

        Returns:
            list[str]: 錯誤代碼字串列表
        """
        return [
            attr_value
            for attr_name, attr_value in error_class.__dict__.items()
            # 排除以 _ 開頭的私有屬性、排除非字串類型的屬性
            if not attr_name.startswith('_') and isinstance(attr_value, str)
        ]

    @pytest.mark.parametrize(
        "error_class,expected_error_codes",
        [
            (
                CORSErrorCode,
                {
                    "ORIGIN_NOT_ALLOWED": "CORS_ORIGIN_NOT_ALLOWED",
                    "METHOD_NOT_ALLOWED": "CORS_METHOD_NOT_ALLOWED",
                    "HEADER_NOT_ALLOWED": "CORS_HEADER_NOT_ALLOWED",
                },
            ),
            (
                CRUDErrorCode,
                {
                    "BAD_REQUEST": "CRUD_BAD_REQUEST",
                    "RECORD_NOT_FOUND": "CRUD_RECORD_NOT_FOUND",
                    "CONSTRAINT_VIOLATION": "CRUD_CONSTRAINT_VIOLATION",
                    "DATABASE_ERROR": "CRUD_DATABASE_ERROR",
                    "CONNECTION_ERROR": "CRUD_CONNECTION_ERROR",
                },
            ),
            (
                RouterErrorCode,
                {
                    "BAD_REQUEST": "ROUTER_BAD_REQUEST",
                    "INVALID_METHOD": "ROUTER_INVALID_METHOD",
                    "INVALID_SCHEDULE_TIME": "ROUTER_INVALID_SCHEDULE_TIME",
                    "AUTHENTICATION_ERROR": "ROUTER_AUTHENTICATION_ERROR",
                    "AUTHORIZATION_ERROR": "ROUTER_AUTHORIZATION_ERROR",
                    "ENDPOINT_NOT_FOUND": "ROUTER_ENDPOINT_NOT_FOUND",
                    "SCHEDULE_NOT_FOUND": "ROUTER_SCHEDULE_NOT_FOUND",
                    "VALIDATION_ERROR": "ROUTER_VALIDATION_ERROR",
                },
            ),
            (
                ServiceErrorCode,
                {
                    "BUSINESS_LOGIC_ERROR": "SERVICE_BUSINESS_LOGIC_ERROR",
                    "SCHEDULE_OVERLAP": "SERVICE_SCHEDULE_OVERLAP",
                    "INVALID_OPERATION": "SERVICE_INVALID_OPERATION",
                    "USER_NOT_FOUND": "SERVICE_USER_NOT_FOUND",
                    "SCHEDULE_NOT_FOUND": "SERVICE_SCHEDULE_NOT_FOUND",
                    "CONFLICT": "SERVICE_CONFLICT",
                    "SCHEDULE_CANNOT_BE_DELETED": "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                },
            ),
            (
                SystemErrorCode,
                {
                    "INTERNAL_ERROR": "INTERNAL_ERROR",
                    "SERVICE_UNAVAILABLE": "SERVICE_UNAVAILABLE",
                    "LIVENESS_CHECK_ERROR": "LIVENESS_CHECK_ERROR",
                    "READINESS_CHECK_ERROR": "READINESS_CHECK_ERROR",
                },
            ),
        ],
    )
    def test_expected_error_code_values(self, error_class, expected_error_codes):
        """測試錯誤代碼預期值 - 驗證實際值與預期值相符。"""
        # GIVEN: 錯誤代碼類別和預期值

        # WHEN: 取得實際值
        for attr_name, expected_value in expected_error_codes.items():
            # THEN: 驗證實際值與預期值相符
            actual_value = getattr(error_class, attr_name)
            assert actual_value == expected_value

    @pytest.mark.parametrize(
        "error_class,expected_prefix",
        [
            (CORSErrorCode, "CORS_"),
            (CRUDErrorCode, "CRUD_"),
            (RouterErrorCode, "ROUTER_"),
            (ServiceErrorCode, "SERVICE_"),
            (SystemErrorCode, None),  # SystemErrorCode 沒有前綴
        ],
    )
    def test_expected_error_code_format(self, error_class, expected_prefix):
        """測試錯誤代碼格式 - 驗證前綴和大小寫格式。"""
        # GIVEN: 錯誤代碼類別

        # WHEN: 取得所有錯誤代碼，過濾掉名稱以 _ 開頭的屬性、非字串類型的屬性
        error_codes = self._get_error_codes(error_class)

        # THEN: 驗證格式
        for code in error_codes:
            if expected_prefix:
                assert "_" in code
                assert code.startswith(expected_prefix)
            # 驗證錯誤代碼必須全部為大寫字母
            assert code.isupper()

    @pytest.mark.parametrize(
        "error_class",
        [
            CORSErrorCode,
            CRUDErrorCode,
            RouterErrorCode,
            ServiceErrorCode,
            SystemErrorCode,
        ],
    )
    def test_expected_error_code_uniqueness(self, error_class):
        """測試錯誤代碼唯一性。"""
        # GIVEN: 錯誤代碼類別

        # WHEN: 取得所有錯誤代碼，過濾掉名稱以 _ 開頭的屬性、非字串類型的屬性
        error_codes = self._get_error_codes(error_class)

        # THEN: 確保唯一性
        assert len(error_codes) == len(set(error_codes))

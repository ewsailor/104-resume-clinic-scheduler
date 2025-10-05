"""錯誤類別模組。

定義系統中使用的所有錯誤類別，按架構層級分類。
"""

# ===== 標準函式庫 =====
from typing import Any

# ===== 第三方套件 =====
from fastapi import status

# ===== 本地模組 =====
from .error_codes.crud import CRUDErrorCode
from .error_codes.router import RouterErrorCode
from .error_codes.service import ServiceErrorCode
from .error_codes.system import SystemErrorCode


class APIError(Exception):
    """API 錯誤基礎類別。"""

    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        details: dict[str, Any] | None = None,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


# ===== CRUD 層級錯誤 =====
class DatabaseError(APIError):
    """資料庫錯誤。"""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=CRUDErrorCode.DATABASE_ERROR,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=details,
        )


# ===== Router 層級錯誤 =====
class BadRequestError(APIError):
    """路由層請求錯誤。"""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=RouterErrorCode.BAD_REQUEST,
            status_code=status.HTTP_400_BAD_REQUEST,
            details=details,
        )


class AuthenticationError(APIError):
    """認證錯誤。"""

    def __init__(
        self,
        message: str = "認證失敗",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=RouterErrorCode.AUTHENTICATION_ERROR,
            status_code=status.HTTP_401_UNAUTHORIZED,
            details=details,
        )


class AuthorizationError(APIError):
    """權限錯誤。"""

    def __init__(
        self,
        message: str = "權限不足",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=RouterErrorCode.AUTHORIZATION_ERROR,
            status_code=status.HTTP_403_FORBIDDEN,
            details=details,
        )


class ValidationError(APIError):
    """資料驗證錯誤。"""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=RouterErrorCode.VALIDATION_ERROR,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            details=details,
        )


# ===== Service 層級錯誤 =====
class BusinessLogicError(APIError):
    """業務邏輯錯誤。"""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=ServiceErrorCode.BUSINESS_LOGIC_ERROR,
            status_code=status.HTTP_400_BAD_REQUEST,
            details=details,
        )


class ScheduleNotFoundError(APIError):
    """時段不存在錯誤。"""

    def __init__(
        self,
        schedule_id: int | str,
        details: dict[str, Any] | None = None,
    ):
        message = f"時段不存在: ID={schedule_id}"
        super().__init__(
            message=message,
            error_code=ServiceErrorCode.SCHEDULE_NOT_FOUND,
            status_code=status.HTTP_404_NOT_FOUND,
            details=details,
        )


class UserNotFoundError(APIError):
    """使用者不存在錯誤。"""

    def __init__(
        self,
        user_id: int | str,
        details: dict[str, Any] | None = None,
    ):
        message = f"使用者不存在: ID={user_id}"
        super().__init__(
            message=message,
            error_code=ServiceErrorCode.USER_NOT_FOUND,
            status_code=status.HTTP_404_NOT_FOUND,
            details=details,
        )


class ConflictError(APIError):
    """資源衝突錯誤。"""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=ServiceErrorCode.CONFLICT,
            status_code=status.HTTP_409_CONFLICT,
            details=details,
        )


class ScheduleCannotBeDeletedError(APIError):
    """時段無法刪除錯誤。"""

    def __init__(
        self,
        schedule_id: int | str,
        details: dict[str, Any] | None = None,
    ):
        message = f"時段無法刪除: ID={schedule_id}"
        super().__init__(
            message=message,
            error_code=ServiceErrorCode.SCHEDULE_CANNOT_BE_DELETED,
            status_code=status.HTTP_409_CONFLICT,
            details=details,
        )


class ScheduleOverlapError(APIError):
    """時段重疊錯誤。"""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=ServiceErrorCode.SCHEDULE_OVERLAP,
            status_code=status.HTTP_409_CONFLICT,
            details=details,
        )


# ===== System 層級 =====
class ServiceUnavailableError(APIError):
    """服務不可用錯誤。"""

    def __init__(
        self,
        message: str = "服務暫時不可用",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code=SystemErrorCode.SERVICE_UNAVAILABLE,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            details=details,
        )

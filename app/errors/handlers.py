"""錯誤處理輔助函式模組。

提供建立特定錯誤實例的輔助函式。
"""

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


# ===== CRUD 層級錯誤 =====
def create_database_error(message: str) -> DatabaseError:
    """建立資料庫錯誤。"""
    return DatabaseError(message)


# ===== Router 層級錯誤 =====
def create_bad_request_error(message: str) -> BadRequestError:
    """建立路由層請求錯誤。"""
    return BadRequestError(message)


def create_authentication_error(message: str) -> AuthenticationError:
    """建立認證錯誤。"""
    return AuthenticationError(message)


def create_authorization_error(message: str) -> AuthorizationError:
    """建立權限錯誤。"""
    return AuthorizationError(message)


def create_validation_error(message: str) -> ValidationError:
    """建立資料驗證錯誤。"""
    return ValidationError(message)


# ===== Service 層級錯誤 =====
def create_business_logic_error(message: str) -> BusinessLogicError:
    """建立業務邏輯錯誤。"""
    return BusinessLogicError(message)


def create_schedule_not_found_error(schedule_id: int | str) -> ScheduleNotFoundError:
    """建立時段不存在錯誤。"""
    return ScheduleNotFoundError(schedule_id)


def create_user_not_found_error(user_id: int | str) -> UserNotFoundError:
    """建立使用者不存在錯誤。"""
    return UserNotFoundError(user_id)


def create_conflict_error(message: str, details: dict | None = None) -> ConflictError:
    """建立資源衝突錯誤。"""
    return ConflictError(message, details=details)


def get_deletion_explanation(status: str) -> str:
    """根據時段狀態提供刪除失敗的解釋。"""
    explanations = {
        "ACCEPTED": "已接受的時段無法刪除，因為雙方已確認面談時間，刪除會影響約定",
        "COMPLETED": "已完成的時段無法刪除，因為面談已完成，屬於歷史記錄，不應刪除",
    }
    return explanations.get(status, "時段狀態不允許刪除")


def create_schedule_cannot_be_deleted_error(
    schedule_id: int | str,
    reason: str | None = None,
    schedule_status: str | None = None,
) -> ScheduleCannotBeDeletedError:
    """建立時段無法刪除錯誤。"""
    details = {}
    if reason:
        details["reason"] = reason
    if schedule_status:
        details["current_status"] = schedule_status
        details["explanation"] = get_deletion_explanation(schedule_status)

    return ScheduleCannotBeDeletedError(schedule_id, details=details)


def create_schedule_overlap_error(
    message: str, overlapping_schedules: list | None = None
) -> ScheduleOverlapError:
    """建立時段重疊錯誤。"""
    details = {}
    if overlapping_schedules:
        details["overlapping_schedules"] = [
            {
                "id": schedule.id,
                "giver_id": schedule.giver_id,
                "date": schedule.date.isoformat(),
                "start_time": schedule.start_time.strftime("%H:%M:%S"),
                "end_time": schedule.end_time.strftime("%H:%M:%S"),
                "status": schedule.status.value if schedule.status else None,
            }
            for schedule in overlapping_schedules
        ]
    return ScheduleOverlapError(message, details=details)


# ===== System 層級錯誤 =====
def create_service_unavailable_error(message: str) -> ServiceUnavailableError:
    """建立服務不可用錯誤。"""
    return ServiceUnavailableError(message)

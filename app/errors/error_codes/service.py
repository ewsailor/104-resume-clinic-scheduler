"""服務層級錯誤代碼。

定義業務邏輯層相關的錯誤代碼。
"""


class ServiceErrorCode:
    """Service 層級錯誤代碼。"""

    # 400 Bad Request - 服務層業務錯誤
    BUSINESS_LOGIC_ERROR = "SERVICE_BUSINESS_LOGIC_ERROR"  # 400 - 業務邏輯錯誤
    SCHEDULE_OVERLAP = "SERVICE_SCHEDULE_OVERLAP"  # 409 - 時段重疊
    INVALID_OPERATION = "SERVICE_INVALID_OPERATION"  # 400 - 無效操作

    # 404 Not Found - 服務層資源錯誤
    USER_NOT_FOUND = "SERVICE_USER_NOT_FOUND"  # 404 - 使用者不存在
    SCHEDULE_NOT_FOUND = "SERVICE_SCHEDULE_NOT_FOUND"  # 404 - 時段不存在

    # 409 Conflict - 服務層衝突錯誤
    CONFLICT = "SERVICE_CONFLICT"  # 409 - 業務邏輯衝突（如重複 email）
    SCHEDULE_CANNOT_BE_DELETED = (
        "SERVICE_SCHEDULE_CANNOT_BE_DELETED"  # 409 - 時段無法刪除
    )

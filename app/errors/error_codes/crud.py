"""CRUD 層級錯誤代碼。

定義資料存取層相關的錯誤代碼。
"""


class CRUDErrorCode:
    """CRUD 層級錯誤代碼。"""

    # 400 Bad Request - CRUD 層請求錯誤
    BAD_REQUEST = "CRUD_BAD_REQUEST"  # 400 - CRUD 操作參數錯誤

    # 404 Not Found - CRUD 層資源錯誤
    RECORD_NOT_FOUND = "CRUD_RECORD_NOT_FOUND"  # 404 - 資料庫記錄不存在

    # 409 Conflict - CRUD 層衝突錯誤
    CONSTRAINT_VIOLATION = "CRUD_CONSTRAINT_VIOLATION"  # 409 - 資料庫約束違反

    # 500 Internal Server Error - CRUD 層資料庫錯誤
    DATABASE_ERROR = "CRUD_DATABASE_ERROR"  # 500 - 資料庫操作失敗
    CONNECTION_ERROR = "CRUD_CONNECTION_ERROR"  # 500 - 資料庫連線錯誤

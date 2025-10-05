"""路由層級錯誤代碼。

定義 API 路由層相關的錯誤代碼。
"""


class RouterErrorCode:
    """Routers 層級錯誤代碼。"""

    # 400 Bad Request - 路由層請求錯誤
    BAD_REQUEST = "ROUTER_BAD_REQUEST"  # 400 - 路由參數格式錯誤
    INVALID_METHOD = "ROUTER_INVALID_METHOD"  # 400 - 不支援的 HTTP 方法
    INVALID_SCHEDULE_TIME = "ROUTER_INVALID_SCHEDULE_TIME"  # 400 - 時段時間邏輯錯誤

    # 401 Unauthorized - 路由層認證錯誤
    AUTHENTICATION_ERROR = "ROUTER_AUTHENTICATION_ERROR"  # 401 - 路由層認證失敗

    # 403 Forbidden - 路由層權限錯誤
    AUTHORIZATION_ERROR = "ROUTER_AUTHORIZATION_ERROR"  # 403 - 路由層權限不足

    # 404 Not Found - 路由層資源錯誤
    ENDPOINT_NOT_FOUND = "ROUTER_ENDPOINT_NOT_FOUND"  # 404 - API 端點不存在
    SCHEDULE_NOT_FOUND = "ROUTER_SCHEDULE_NOT_FOUND"  # 404 - 時段不存在

    # 422 Unprocessable Entity - 路由層驗證錯誤
    VALIDATION_ERROR = "ROUTER_VALIDATION_ERROR"  # 422 - 路由層資料驗證失敗

"""CORS 層級錯誤代碼。

定義跨域請求相關的錯誤代碼。
"""


class CORSErrorCode:
    """CORS 層級錯誤代碼。"""

    # 403 Forbidden - CORS 層權限錯誤
    ORIGIN_NOT_ALLOWED = "CORS_ORIGIN_NOT_ALLOWED"  # 403 - 來源網域不被允許
    METHOD_NOT_ALLOWED = "CORS_METHOD_NOT_ALLOWED"  # 403 - HTTP 方法不被允許
    HEADER_NOT_ALLOWED = "CORS_HEADER_NOT_ALLOWED"  # 403 - 請求標頭不被允許

"""錯誤處理中間件。

提供統一的錯誤處理機制。
"""

# ===== 標準函式庫 =====
import logging
from typing import Callable

# ===== 第三方套件 =====
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# ===== 本地模組 =====
from app.errors import format_error_response

# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """錯誤處理中間件。"""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """處理請求並捕獲錯誤。"""
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            return await self._handle_exception(request, exc)

    async def _handle_exception(self, request: Request, exc: Exception) -> JSONResponse:
        """處理異常並返回標準化的錯誤回應。"""

        error_response = format_error_response(exc)

        # 從格式化結果中取得狀態碼
        status_code = error_response["error"]["status_code"]

        logger.error(f"錯誤: {request.method} {request.url.path} - {str(exc)}")

        # 創建 JSONResponse 並保留 CORS 標頭
        response = JSONResponse(status_code=status_code, content=error_response)

        # 保留原始請求的 CORS 相關標頭
        origin = request.headers.get("origin")
        if origin:
            response.headers["access-control-allow-origin"] = origin
            response.headers["access-control-allow-credentials"] = "true"
            response.headers["access-control-allow-methods"] = (
                "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            )
            response.headers["access-control-allow-headers"] = "*"

        return response


def setup_error_handlers(app: FastAPI) -> None:
    """設定全域錯誤處理器。"""
    app.add_middleware(ErrorHandlerMiddleware)

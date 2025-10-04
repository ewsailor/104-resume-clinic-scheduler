"""錯誤格式化模組。

提供錯誤訊息的格式化功能。
"""

# ===== 標準函式庫 =====
import logging
from typing import Any

# ===== 第三方套件 =====
from fastapi import HTTPException

# ===== 本地模組 =====
# 絕對路徑導入（跨模組）
from app.utils.timezone import get_utc_timestamp

# 相對路徑導入（同模組）
from .exceptions import APIError

# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


def format_error_response(error: Exception) -> dict[str, Any]:
    """格式化錯誤回應。"""
    logger.info(f"格式化錯誤: {type(error).__name__}")

    # 處理自定義 APIError：從 APIError 物件中取出 message、status_code、error_code 和 details 等屬性，並回傳包含這些資訊的字典
    if isinstance(error, APIError):
        return {
            "error": {
                "message": error.message,
                "status_code": error.status_code,
                "code": error.error_code,
                "timestamp": get_utc_timestamp(),
                "details": error.details,
            }
        }

    # 處理非自定義 APIError，被 FastAPI 內建的 HTTPException 捕捉的錯誤
    if isinstance(error, HTTPException):
        # 如果 HTTPException 的 detail 屬性存在，則使用 detail 屬性作為錯誤訊息，否則使用預設的 "請求錯誤"
        message = str(error.detail) if error.detail else "請求錯誤"
        return {
            "error": {
                "message": message,
                "status_code": error.status_code,
                "code": f"HTTP_{error.status_code}",
                "timestamp": get_utc_timestamp(),
                "details": {"detail": error.detail} if error.detail else {},
            }
        }

    # 處理其他錯誤：未被自定義 APIError 或 FastAPI HTTPException 捕捉的錯誤
    return {
        "error": {
            "message": str(error),
            "status_code": 500,
            "code": "INTERNAL_ERROR",
            "timestamp": get_utc_timestamp(),
            "details": {"error": str(error)},
        }
    }

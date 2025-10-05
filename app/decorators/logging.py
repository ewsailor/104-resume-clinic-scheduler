"""日誌裝飾器模組。

提供各種日誌記錄裝飾器，用於記錄函式執行情況。
"""

# ===== 標準函式庫 =====
from functools import wraps
import logging
from typing import Any, Callable

# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


def log_operation(operation_name: str) -> Callable:
    """操作日誌裝飾器。

    記錄操作的開始、成功和失敗狀態。
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info(f"開始{operation_name}")

            try:
                result = func(*args, **kwargs)
                logger.info(f"{operation_name}成功")
                return result
            except Exception as e:
                logger.error(f"{operation_name}失敗: {str(e)}")
                raise e

        return wrapper

    return decorator

"""裝飾器模組。

提供各種裝飾器功能，包括錯誤處理、日誌記錄等。
"""

# ===== 本地模組 =====
from .error_handlers import (
    handle_api_errors_async,
    handle_generic_errors_async,
    handle_generic_errors_sync,
    handle_service_errors_sync,
)
from .logging import (
    log_operation,
)

__all__ = [
    # 錯誤處理裝飾器
    "handle_api_errors_async",
    "handle_generic_errors_sync",
    "handle_generic_errors_async",
    "handle_service_errors_sync",
    # 日誌記錄裝飾器
    "log_operation",
]

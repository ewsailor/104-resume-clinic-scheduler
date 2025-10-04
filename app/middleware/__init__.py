"""中間件套件。

包含所有 FastAPI 應用程式的中間件，如 CORS、認證、日誌等。
"""

# ===== 本地模組 =====
from .cors import setup_cors_middleware
from .error_handler import setup_error_handlers

__all__ = [
    # CORS 中間件
    "setup_cors_middleware",
    # 錯誤處理中間件
    "setup_error_handlers",
]

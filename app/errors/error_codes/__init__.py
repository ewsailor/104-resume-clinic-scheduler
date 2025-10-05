"""錯誤代碼模組。

整合所有層級的錯誤代碼，提供統一的錯誤代碼管理。

包含：
- 路由層錯誤代碼
- 服務層錯誤代碼
- CRUD 層錯誤代碼
- CORS 錯誤代碼
- 系統錯誤代碼
"""

# ===== 本地模組 =====
from .cors import CORSErrorCode
from .crud import CRUDErrorCode
from .router import RouterErrorCode
from .service import ServiceErrorCode
from .system import SystemErrorCode

# 匯出所有錯誤代碼類別
__all__ = [
    "RouterErrorCode",
    "ServiceErrorCode",
    "CRUDErrorCode",
    "CORSErrorCode",
    "SystemErrorCode",
]

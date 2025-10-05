"""路由模組套件。

包含所有應用程式的路由定義，包括：
- 主要路由 (main.py)
- 健康檢查路由 (health.py)
- API 路由 (api/)
"""

# ===== 本地模組 =====
from .api import api_router
from .health import router as health_router
from .main import router as main_router

__all__ = [
    # 對外匯出的路由器
    "api_router",
    "health_router",
    "main_router",
]

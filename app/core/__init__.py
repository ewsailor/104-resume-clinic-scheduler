"""核心模組。

提供應用程式的核心功能，包括：
- 應用程式設定管理
- 專案版本資訊
- 環境配置處理
"""

# ===== 本地模組 =====
from .settings import get_project_version, Settings, settings

__all__ = [
    # 設定管理
    "Settings",
    "settings",
    "get_project_version",
]

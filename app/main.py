"""FastAPI 應用程式主入口。

104 履歷診療室 - 站內諮詢時間媒合系統：讓 Giver、Taker 在平台內，方便地設定可面談時間，並完成配對媒合。
"""

# ===== 本地模組 =====
from app.core import settings
from app.factory import create_app, create_static_files, create_templates
from app.middleware.cors import log_app_startup, setup_cors_middleware
from app.middleware.error_handler import setup_error_handlers
from app.routers import health_router, main_router  # api_router

# ===== 應用程式初始化 =====
# 建立應用程式實例
app = create_app(settings)

# 記錄應用程式啟動資訊
log_app_startup(app)

# CORS 中間件設定
setup_cors_middleware(app)

# 錯誤處理器設定
setup_error_handlers(app)

# ===== 應用程式狀態設定 =====
# 建立模板引擎實例
templates = create_templates(settings)

# 將 templates 設定到應用程式狀態中，用依賴注入解決循環匯入問題
app.state.templates = templates

# ===== 路由註冊 =====
app.include_router(main_router)
app.include_router(health_router)
# app.include_router(api_router)

# ===== 靜態檔案掛載 =====
app.mount(settings.static_url, create_static_files(settings), name=settings.static_name)

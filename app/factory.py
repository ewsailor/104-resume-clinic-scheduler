"""應用程式工廠模組。

負責建立和配置 FastAPI 應用程式的各個組件，包括靜態檔案服務、模板引擎等。
"""

# ===== 第三方套件 =====
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ===== 本地模組 =====
from app.core.settings import Settings
from app.decorators import handle_generic_errors_sync

# from app.middleware.cors import log_app_startup, setup_cors_middleware


def create_static_files(settings: Settings) -> StaticFiles:
    """建立並配置靜態檔案服務。"""
    return StaticFiles(directory=str(settings.static_dir))


def create_templates(settings: Settings) -> Jinja2Templates:
    """建立並配置 Jinja2 模板引擎。"""
    return Jinja2Templates(directory=str(settings.templates_dir))


@handle_generic_errors_sync("建立 FastAPI 應用程式")
def create_app(settings: Settings) -> FastAPI:
    """建立並配置 FastAPI 應用程式。"""
    # 根據環境決定是否顯示 API 文件
    docs_url = settings.docs_url if settings.debug else None
    redoc_url = settings.redoc_url if settings.debug else None
    openapi_url = settings.openapi_url if settings.debug else None

    # 根據環境設定伺服器資訊
    servers = []

    # 開發環境：顯示開發伺服器
    if settings.debug:
        servers.append(
            {
                "url": settings.server_url,
                "description": settings.server_description,
            }
        )

    # 可以根據需要添加其他環境（僅在開發模式下）
    # 注意：生產環境不應暴露多個伺服器 URL
    if settings.debug and settings.app_env == "development":
        # 可以添加測試環境（如果需要）
        # servers.append({
        #     "url": "https://test-api.example.com",
        #     "description": "測試環境",
        # })
        pass

    # 建立 FastAPI 應用程式
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
        debug=settings.debug,
        docs_url=docs_url,
        redoc_url=redoc_url,
        openapi_url=openapi_url,
        servers=servers,
        contact={
            "name": "鍾郡荃 Oscar",
            "email": "ew12136@gmail.com",
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT",
        },
    )

    # 記錄應用程式啟動資訊
    # log_app_startup(app)

    # CORS 中間件設定
    # setup_cors_middleware(app)

    # 掛載靜態檔案服務
    app.mount(
        settings.static_url, create_static_files(settings), name=settings.static_name
    )

    return app

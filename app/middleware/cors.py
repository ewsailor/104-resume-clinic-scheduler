"""CORS 中間件。

提供基本的跨來源資源共用設定。
"""

# ===== 標準函式庫 =====
import logging

# ===== 第三方套件 =====
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


def log_app_startup(app: FastAPI) -> None:
    """記錄應用程式啟動資訊。"""
    logger.info("===== 應用程式啟動完成 ======")


def setup_cors_middleware(app: FastAPI) -> None:
    """設定 CORS 中間件。"""
    origins = [
        "http://localhost:3000",  # React 開發伺服器
        "http://localhost:8000",  # FastAPI 開發伺服器
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]
    logger.info("CORS 中間件設定完成")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    headers = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=methods,
        allow_headers=headers,
    )

"""API 路由模組集中匯入點。

匯入所有 API 相關的路由器，提供統一的 API 介面。

包含：
- 時段管理 API（schedule_router）
"""

# ===== 第三方套件 =====
from fastapi import APIRouter

# ===== 本地模組 =====
from .schedule import router as schedule_router

# 建立 API 路由器
api_router = APIRouter()

# 註冊所有 API 路由
api_router.include_router(schedule_router)

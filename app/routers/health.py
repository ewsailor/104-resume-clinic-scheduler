"""健康檢查路由模組。

包含存活探測和就緒探測等端點。
"""

# ===== 第三方套件 =====
from fastapi import APIRouter, HTTPException, status

# ===== 本地模組 =====
from app.database import check_db_connection

router = APIRouter(tags=["Health Check"])


@router.get(
    "/healthz",
    status_code=status.HTTP_200_OK,
    summary="存活探測檢查",
    description="""
## 功能簡介
- 檢查應用程式是否存活、正在運行，用於 Kubernetes 的 liveness probe
- 不包含外部依資料庫、快取等檢查
- 僅檢查應用程式進程狀態

### 使用場景
- Kubernetes 容器健康檢查
- 負載平衡器健康檢查
- 應用程式監控系統

### 回應狀態
- **200 OK**: 應用程式存活、正常運行
- **500 Internal Server Error**: 應用程式異常、未正常運行
    """,
    responses={
        200: {
            "description": "應用程式存活、正常運行",
            "content": {"application/json": {"example": {"status": "healthy"}}},
        },
        500: {
            "description": "存活探測檢查錯誤：應用程式異常、未正常運行",
            "content": {"application/json": {"example": {"status": "unhealthy"}}},
        },
    },
)
async def liveness_probe() -> dict[str, str]:
    """存活探測：用於 Kubernetes 的 liveness probe，檢查應用程式是否存活、正在運行。
    不包含外部依資料庫、快取等檢查，只檢查應用程式進程狀態。

    Returns:
        dict[str, str]:只包含基本狀態資訊，避免暴露敏感資訊。
    """
    # 基本存活檢查：函式能執行到這裡，表示應用程式存活
    # 不需要 try-except：連這個都失敗表示應用程式真的死了，應該讓它失敗，避免讓它繼續運行
    return {"status": "healthy"}


@router.get(
    "/readyz",
    status_code=status.HTTP_200_OK,
    summary="就緒探測檢查",
    description="""
## 功能簡介
- 檢查應用程式所有外部依賴，是否已準備好處理請求，用於 Kubernetes 的 readiness probe
- 外部依賴如資料庫、快取、外部 API 等
- 檢查應用程式進程狀態、資料庫連線、基本查詢，如連線失敗會拋出異常

### 使用場景
- Kubernetes 容器就緒檢查
- 藍綠部署時的流量切換
- 負載平衡器流量分配

### 檢查項目
- **應用程式**: 檢查應用程式進程狀態
- **資料庫**: 檢查資料庫連線和基本查詢
- **快取** (未來): 檢查 Redis 連線狀態
- **外部 API** (未來): 檢查關鍵外部服務連線

### 回應狀態
- **200 OK**: 應用程式準備就緒
- **503 Service Unavailable**: 應用程式未準備就緒
    """,
    responses={
        200: {
            "description": "應用程式準備就緒",
            "content": {"application/json": {"example": {"status": "healthy"}}},
        },
        503: {
            "description": "就緒探測檢查錯誤：應用程式未準備就緒",
            "content": {"application/json": {"example": {"status": "unhealthy"}}},
        },
    },
)
async def readiness_probe() -> dict[str, str]:
    """就緒探測：用於 Kubernetes 的 readiness probe，檢查應用程式所有外部依賴如資料庫、快取、外部 API 等，是否已經準備好處理請求。

    Returns:
        dict[str, str]:只包含基本狀態資訊，避免暴露敏感資訊。
    """
    # 檢查真實資料庫連線（如果連線失敗會拋出異常）
    try:
        check_db_connection()
    except Exception:
        # 不暴露具體錯誤資訊，避免資訊洩露
        raise HTTPException(status_code=503, detail="Service Unavailable")

    return {"status": "healthy"}

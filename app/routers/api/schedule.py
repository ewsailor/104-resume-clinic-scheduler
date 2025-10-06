"""時段管理 API 路由模組。

提供時段相關的 API 端點，包括建立、查詢、更新和刪除時段。
"""

# ===== 第三方套件 =====
from fastapi import APIRouter, Depends, Path, Query, status
from sqlalchemy.orm import Session

# ===== 本地模組 =====
from app.database import get_db
from app.decorators import handle_api_errors_async
from app.enums.models import ScheduleStatusEnum
from app.errors import create_bad_request_error
from app.schemas import (
    ScheduleCreateRequest,
    ScheduleDeleteRequest,
    SchedulePartialUpdateRequest,
    ScheduleResponse,
)
from app.services import schedule_service

router = APIRouter(prefix="/api/v1", tags=["Schedules"])


@router.post(
    "/schedules",
    response_model=list[ScheduleResponse],
    status_code=status.HTTP_201_CREATED,
    summary="建立多個時段",
    description="""
## 功能簡介
- Giver、Taker 建立方便面談的時段

### 使用場景
- Giver 提供可預約的時段，讓 Taker 預約面談
- Taker 提供方便的時段，待 Giver 回覆是否方便面談
  - 因 Giver 尚未提供可預約的時段，Taker 無法預約面談
  - 因 Giver 已提供的方便時段，Taker 均不方便面談

### 回應狀態
- **201 Created**: 成功建立時段
- **400 Bad Request**: 時段邏輯錯誤
- **409 Conflict**: 時段衝突錯誤
- **422 Unprocessable Entity**: 參數驗證錯誤
    """,
    responses={
        201: {
            "description": "成功建立時段",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "giver_id": 1,
                            "taker_id": 1,
                            "status": "PENDING",
                            "date": "2024-01-01",
                            "start_time": "09:00:00",
                            "end_time": "10:00:00",
                            "note": "成功建立時段",
                            "created_at": "2024-01-01T00:00:00Z",
                            "created_by": 1,
                            "created_by_role": "TAKER",
                            "updated_at": "2024-01-01T00:00:00Z",
                            "updated_by": 1,
                            "updated_by_role": "TAKER",
                            "deleted_at": "null",
                            "deleted_by": "null",
                            "deleted_by_role": "null",
                        }
                    ]
                }
            },
        },
        400: {
            "description": "時段邏輯錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "開始時間必須早於結束時間",
                            "status_code": 400,
                            "code": "ROUTER_BAD_REQUEST",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {},
                        }
                    }
                }
            },
        },
        409: {
            "description": "時段衝突錯誤（Service 拋出錯誤，由 Route 捕捉）",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "檢測到 1 個重疊時段，請調整時段之時間",
                            "status_code": 409,
                            "code": "SERVICE_SCHEDULE_OVERLAP",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {
                                "overlapping_schedules": [
                                    {
                                        "id": 123,
                                        "giver_id": 1,
                                        "date": "2024-01-01",
                                        "start_time": "08:00:00",
                                        "end_time": "12:00:00",
                                        "status": "AVAILABLE",
                                    }
                                ]
                            },
                        }
                    }
                }
            },
        },
        422: {
            "description": "參數驗證錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "validation_error_type",
                                "loc": ["path", "to", "field"],
                                "msg": "具體錯誤訊息",
                                "input": "無效的輸入值",
                                "ctx": {"error": "錯誤上下文"},
                            }
                        ]
                    }
                }
            },
        },
    },
)
@handle_api_errors_async()
async def create_schedules(
    request: ScheduleCreateRequest,
    db: Session = Depends(get_db),
) -> list[ScheduleResponse]:
    """建立多個時段：批量建立時段記錄，用於 Giver、Taker 建立方便面談的時段。

    Args:
        request (ScheduleCreateRequest): 建立時段請求資料。
        db (Session): 資料庫會話。

    Returns:
        list[ScheduleResponse]: 建立的時段列表。
    """
    # 驗證每個時段的時間邏輯
    for schedule in request.schedules:
        if schedule.start_time >= schedule.end_time:
            raise create_bad_request_error("開始時間必須早於結束時間")

    schedules = schedule_service.create_schedules(
        db,
        request.schedules,
        created_by=request.created_by,
        created_by_role=request.created_by_role,
    )

    # 資料序列化：使用 Pydantic 將 SQLAlchemy ORM 模型轉換為 API 回應格式
    return [ScheduleResponse.model_validate(schedule) for schedule in schedules]


@router.get(
    "/schedules",
    response_model=list[ScheduleResponse],
    status_code=status.HTTP_200_OK,
    summary="取得時段列表",
    description="""
## 功能簡介
- 查詢時段列表，支援多種篩選條件
- 可根據 Giver、Taker、狀態進行篩選

### 使用場景
- Taker 查看 Giver 提供的可預約時段，以利預約面談
- Giver 查看 Taker 提供的時段，以利回覆自己是否方便面談
- 系統管理員查看所有尚未回覆的時段，以利發送提醒訊息給 Giver、Taker

### 查詢參數
- 不提供參數：取得所有時段
- **giver_id**: 篩選特定 Giver 的時段（必須大於 0）
- **taker_id**: 篩選特定 Taker 的時段（必須大於 0）
- **status_filter**: 篩選特定狀態的時段（DRAFT、AVAILABLE、PENDING、ACCEPTED、REJECTED、CANCELLED、COMPLETED）

### 回應狀態
- **200 OK**: 成功取得時段列表
- **422 Unprocessable Entity**: 參數驗證錯誤
    """,
    responses={
        200: {
            "description": "成功取得時段列表",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "giver_id": 1,
                            "taker_id": 1,
                            "status": "PENDING",
                            "date": "2024-01-01",
                            "start_time": "09:00:00",
                            "end_time": "10:00:00",
                            "note": "成功取得時段列表",
                            "created_at": "2024-01-01T00:00:00Z",
                            "created_by": 1,
                            "created_by_role": "TAKER",
                            "updated_at": "2024-01-01T00:00:00Z",
                            "updated_by": 1,
                            "updated_by_role": "TAKER",
                            "deleted_at": "null",
                            "deleted_by": "null",
                            "deleted_by_role": "null",
                        }
                    ]
                }
            },
        },
        422: {
            "description": "參數驗證錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "validation_error_type",
                                "loc": ["path", "to", "field"],
                                "msg": "具體錯誤訊息",
                                "input": "無效的輸入值",
                                "ctx": {"error": "錯誤上下文"},
                            }
                        ]
                    }
                }
            },
        },
    },
)
@handle_api_errors_async()
async def list_schedules(
    giver_id: int | None = Query(None, gt=0, description="Giver ID，必須大於 0"),
    taker_id: int | None = Query(None, gt=0, description="Taker ID，必須大於 0"),
    status_filter: ScheduleStatusEnum | None = None,
    db: Session = Depends(get_db),
) -> list[ScheduleResponse]:
    """取得時段列表：查詢時段列表，支援多種篩選條件。

    Args:
        giver_id (int | None): Giver ID 篩選條件，必須大於 0。
        taker_id (int | None): Taker ID 篩選條件，必須大於 0。
        status_filter (ScheduleStatusEnum | None): 狀態篩選條件。
        db (Session): 資料庫會話。

    Returns:
        list[ScheduleResponse]: 時段列表。
    """
    schedules = schedule_service.list_schedules(
        db,
        giver_id,
        taker_id,
        status_filter,
    )

    # 資料序列化：使用 Pydantic 將 SQLAlchemy ORM 模型轉換為 API 回應格式
    return [ScheduleResponse.model_validate(schedule) for schedule in schedules]


@router.get(
    "/schedules/{schedule_id}",
    response_model=ScheduleResponse,
    status_code=status.HTTP_200_OK,
    summary="取得單一時段",
    description="""
## 功能簡介
- 根據時段 ID 取得單一時段的完整資訊

### 使用場景
- 查看時段詳細資訊
- 查看時段回覆狀態是否有更新

### 路徑參數
- **schedule_id**: 時段 ID（必填，必須大於 0）

### 回應狀態
- **200 OK**: 成功取得時段資訊
- **404 Not Found**: 時段不存在錯誤
- **422 Unprocessable Entity**: 參數驗證錯誤
    """,
    responses={
        200: {
            "description": "成功取得時段資訊",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "giver_id": 1,
                        "taker_id": 1,
                        "status": "PENDING",
                        "date": "2024-01-01",
                        "start_time": "09:00:00",
                        "end_time": "10:00:00",
                        "note": "成功取得時段資訊",
                        "created_at": "2024-01-01T00:00:00Z",
                        "created_by": 1,
                        "created_by_role": "TAKER",
                        "updated_at": "2024-01-01T00:00:00Z",
                        "updated_by": 1,
                        "updated_by_role": "TAKER",
                        "deleted_at": "null",
                        "deleted_by": "null",
                        "deleted_by_role": "null",
                    }
                }
            },
        },
        404: {
            "description": "時段不存在錯誤（Service 拋出錯誤，由 Route 捕捉）",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "時段不存在: ID=schedule_id",
                            "status_code": 404,
                            "code": "SERVICE_SCHEDULE_NOT_FOUND",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {},
                        }
                    }
                }
            },
        },
        422: {
            "description": "參數驗證錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "validation_error_type",
                                "loc": ["path", "to", "field"],
                                "msg": "具體錯誤訊息",
                                "input": "無效的輸入值",
                                "ctx": {"error": "錯誤上下文"},
                            }
                        ]
                    }
                }
            },
        },
    },
)
@handle_api_errors_async()
async def get_schedule(
    schedule_id: int = Path(..., gt=0, description="時段 ID，必填，必須大於 0"),
    db: Session = Depends(get_db),
) -> ScheduleResponse:
    """取得單一時段：根據時段 ID 取得單一時段的詳細資訊。

    Args:
        schedule_id (int): 時段 ID，必填，必須大於 0。
        db (Session): 資料庫會話。

    Returns:
        ScheduleResponse: 時段詳細資訊。
    """
    schedule = schedule_service.get_schedule(db, schedule_id)
    return ScheduleResponse.model_validate(schedule)


@router.patch(
    "/schedules/{schedule_id}",
    response_model=ScheduleResponse,
    status_code=status.HTTP_200_OK,
    summary="部分更新時段",
    description="""
## 功能簡介
- 部分更新時段資訊，只更新提供的欄位

### 使用場景
- Giver 編輯尚未公開給 Taker 預約的諮詢時間，以利因應行程變動
- Taker 編輯尚未送出給 Giver 的諮詢時間，以利因應行程變動
- 系統管理員調整時段資訊

### 路徑參數
- **schedule_id**: 時段 ID（必填，必須大於 0）

### 回應狀態
- **200 OK**: 成功更新時段
- **400 Bad Request**: 更新資料無效
- **404 Not Found**: 時段不存在錯誤
- **409 Conflict**: 時段衝突錯誤
- **422 Unprocessable Entity**: 參數驗證錯誤
    """,
    responses={
        200: {
            "description": "成功更新時段",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "giver_id": 1,
                        "taker_id": 1,
                        "status": "PENDING",
                        "date": "2024-01-01",
                        "start_time": "09:00:00",
                        "end_time": "10:00:00",
                        "note": "成功更新時段",
                        "created_at": "2024-01-01T00:00:00Z",
                        "created_by": 1,
                        "created_by_role": "TAKER",
                        "updated_at": "2024-01-01T09:00:00Z",
                        "updated_by": 1,
                        "updated_by_role": "TAKER",
                        "deleted_at": "null",
                        "deleted_by": "null",
                        "deleted_by_role": "null",
                    }
                }
            },
        },
        400: {
            "description": "更新資料錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "更新資料錯誤",
                            "status_code": 400,
                            "code": "ROUTER_BAD_REQUEST",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {},
                        }
                    }
                }
            },
        },
        404: {
            "description": "時段不存在錯誤（Service 拋出錯誤，由 Route 捕捉）",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "時段不存在: ID=schedule_id",
                            "status_code": 404,
                            "code": "SERVICE_SCHEDULE_NOT_FOUND",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {},
                        }
                    }
                }
            },
        },
        409: {
            "description": "時段衝突錯誤（Service 拋出錯誤，由 Route 捕捉）",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "更新時段 ID=schedule_id 時，檢測到 {len(overlapping_schedules)} 個重疊時段，請調整時段之時間",
                            "status_code": 409,
                            "code": "SERVICE_SCHEDULE_OVERLAP",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {
                                "overlapping_schedules": [
                                    {
                                        "id": 1,
                                        "giver_id": 1,
                                        "date": "2024-01-01",
                                        "start_time": "08:00:00",
                                        "end_time": "12:00:00",
                                        "status": "AVAILABLE",
                                    }
                                ]
                            },
                        }
                    }
                }
            },
        },
        422: {
            "description": "參數驗證錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "validation_error_type",
                                "loc": ["path", "to", "field"],
                                "msg": "具體錯誤訊息",
                                "input": "無效的輸入值",
                                "ctx": {"error": "錯誤上下文"},
                            }
                        ]
                    }
                }
            },
        },
    },
)
@handle_api_errors_async()
async def update_schedule(
    request: SchedulePartialUpdateRequest,
    schedule_id: int = Path(..., gt=0, description="時段 ID，必填，必須大於 0"),
    db: Session = Depends(get_db),
) -> ScheduleResponse:
    """部分更新時段：只更新提供的欄位。

    Args:
        request (SchedulePartialUpdateRequest): 更新請求資料。
        schedule_id (int): 時段 ID，必填，必須大於 0。
        db (Session): 資料庫會話。

    Returns:
        ScheduleResponse: 更新後的時段資訊。
    """
    # 將 Pydantic 模型的物件，轉換為字典格式，只包含非 None 的欄位，避免把「空值」也更新到資料庫
    # 使用 by_alias=True 來獲得別名形式的字典，這樣 date 欄位會以別名形式出現
    update_data = request.schedule.model_dump(by_alias=True, exclude_none=True)
    # 處理 date 欄位的別名 - 將 date 轉換為 schedule_date，以符合資料庫或後端函式期望的欄位名稱
    if "date" in update_data:
        update_data["schedule_date"] = update_data.pop("date")

    schedule = schedule_service.update_schedule(
        db,
        schedule_id,
        updated_by=request.updated_by,
        updated_by_role=request.updated_by_role,
        **update_data,  # 字典解包：傳遞更新資料
    )
    return ScheduleResponse.model_validate(schedule)


@router.delete(
    "/schedules/{schedule_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="刪除時段",
    description="""
## 功能簡介
- 軟刪除指定的時段記錄

### 使用場景
- Giver 刪除不再方便提供的時間
- Taker 刪除不再方便提供的時間
- 系統管理員清理無效時段
- 批量清理過期時段

### 路徑參數
- **schedule_id**: 時段 ID（必填，必須大於 0）

### 回應狀態
- **204 No Content**: 成功刪除時段
- **404 Not Found**: 時段不存在錯誤
- **409 Conflict**: 時段無法刪除錯誤
- **422 Unprocessable Entity**: 參數驗證錯誤
    """,
    responses={
        204: {
            "description": "成功刪除時段",
        },
        404: {
            "description": "時段不存在錯誤（Service 拋出錯誤，由 Route 捕捉）",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "時段不存在: ID=schedule_id",
                            "status_code": 404,
                            "code": "SERVICE_SCHEDULE_NOT_FOUND",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {},
                        }
                    }
                }
            },
        },
        409: {
            "description": "時段無法刪除錯誤（Service 拋出錯誤，由 Route 捕捉）",
            "content": {
                "application/json": {
                    "example": {
                        "error": {
                            "message": "時段無法刪除: ID=schedule_id",
                            "status_code": 409,
                            "code": "SERVICE_SCHEDULE_CANNOT_BE_DELETED",
                            "timestamp": "2024-01-01T00:00:00Z",
                            "details": {
                                "reason": "狀態不允許刪除",
                                "current_status": "ACCEPTED",
                                "explanation": "已接受的時段無法刪除，因為雙方已確認面談時間，刪除會影響約定",
                            },
                        }
                    }
                }
            },
        },
        422: {
            "description": "參數驗證錯誤",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "validation_error_type",
                                "loc": ["path", "to", "field"],
                                "msg": "具體錯誤訊息",
                                "input": "無效的輸入值",
                                "ctx": {"error": "錯誤上下文"},
                            }
                        ]
                    }
                }
            },
        },
    },
)
@handle_api_errors_async()
async def delete_schedule(
    request: ScheduleDeleteRequest,
    schedule_id: int = Path(..., gt=0, description="時段 ID，必填，必須大於 0"),
    db: Session = Depends(get_db),
) -> None:
    """刪除時段：刪除指定的時段記錄。

    Args:
        request (ScheduleDeleteRequest): 刪除請求資料。
        schedule_id (int): 時段 ID，必填，必須大於 0。
        db (Session): 資料庫會話。

    Returns:
        None: 刪除成功無回傳內容。
    """
    schedule_service.delete_schedule(
        db,
        schedule_id,
        deleted_by=request.deleted_by,
        deleted_by_role=request.deleted_by_role,
    )

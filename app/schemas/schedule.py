"""時段相關的 Pydantic 資料模型。

定義時段管理相關的請求和回應模型。
"""

# ===== 標準函式庫 =====
from datetime import date, datetime, time

# ===== 第三方套件 =====
from pydantic import BaseModel, ConfigDict, Field

# ===== 本地模組 =====
from app.enums.models import ScheduleStatusEnum, UserRoleEnum


# ===== 基礎模型 =====
class ScheduleBase(BaseModel):
    """單一時段資料模型。"""

    giver_id: int = Field(
        ..., description="Giver ID", gt=0, json_schema_extra={"example": 1}
    )
    taker_id: int | None = Field(
        None,
        description="Taker ID，可為 NULL（表示 Giver 提供時段供 Taker 預約）",
        gt=0,
        json_schema_extra={"example": 2},
    )
    status: ScheduleStatusEnum = Field(
        default=ScheduleStatusEnum.DRAFT,
        description="時段狀態（後端會根據操作者角色自動決定：GIVER→AVAILABLE，TAKER→PENDING，其他→DRAFT）",
        json_schema_extra={"example": ScheduleStatusEnum.AVAILABLE},
    )
    schedule_date: date = Field(
        ...,
        description="時段日期",
        alias="date",
        json_schema_extra={"example": "2024-01-01"},
    )
    start_time: time = Field(
        ...,
        description="開始時間",
        json_schema_extra={"example": "09:00:00"},
    )
    end_time: time = Field(
        ...,
        description="結束時間",
        json_schema_extra={"example": "10:00:00"},
    )
    note: str | None = Field(
        None,
        description="備註",
        max_length=255,
        json_schema_extra={"example": "下週要面試，希望能請教面試技巧"},
    )

    model_config = ConfigDict(
        from_attributes=True,  # 允許 Pydantic 從 ORM 物件（而非 dict）的屬性中讀取資料，以進行驗證和序列化
        populate_by_name=True,  # 若欄位設定了別名，原欄位名稱、別名都能被正確解析
        # 不設定 extra，保持預設 extra="forbid"，當輸入資料包含模型未定義的欄位時，拋出驗證錯誤
    )


# class ScheduleUpdateBase(BaseModel):
#     """部分更新時段的基礎模型 - 所有欄位都是可選的。"""

#     giver_id: int | None = Field(
#         None, description="Giver ID", gt=0, json_schema_extra={"example": 1}
#     )
#     taker_id: int | None = Field(
#         None, description="Taker ID", gt=0, json_schema_extra={"example": 2}
#     )
#     status: ScheduleStatusEnum | None = Field(
#         default=None,
#         description="時段狀態（可選，如果不傳此欄位則不更新狀態，如果傳 null 則會拋出驗證錯誤）",
#         json_schema_extra={"example": ScheduleStatusEnum.PENDING},
#     )
#     schedule_date: date | None = Field(
#         None,
#         description="時段日期",
#         alias="date",
#         json_schema_extra={"example": "2024-01-01"},
#     )
#     start_time: time | None = Field(
#         None,
#         description="開始時間",
#         json_schema_extra={"example": "14:00:00"},
#     )
#     end_time: time | None = Field(
#         None,
#         description="結束時間",
#         json_schema_extra={"example": "15:00:00"},
#     )
#     note: str | None = Field(
#         None,
#         description="備註",
#         max_length=255,
#         json_schema_extra={"example": "下週要面試，希望能請教面試技巧"},
#     )


# ===== 請求模型 =====
class ScheduleCreateRequest(BaseModel):
    """批量建立時段的 API 請求模型。"""

    schedules: list[ScheduleBase] = Field(
        ...,
        description="要建立的時段列表",
        json_schema_extra={
            "example": [
                {
                    "giver_id": 1,
                    "taker_id": 1,
                    "status": "PENDING",
                    "date": "2024-01-01",
                    "start_time": "09:00:00",
                    "end_time": "10:00:00",
                    "note": "建立第 1 個測試時段",
                    "created_by_role": "TAKER",
                    "updated_by_role": "TAKER",
                },
                {
                    "giver_id": 2,
                    "taker_id": 1,
                    "status": "PENDING",
                    "date": "2024-01-01",
                    "start_time": "11:00:00",
                    "end_time": "12:00:00",
                    "note": "建立第 2 個測試時段",
                    "created_by_role": "TAKER",
                    "updated_by_role": "TAKER",
                },
            ]
        },
    )
    created_by: int = Field(
        ..., description="建立者的 ID", gt=0, json_schema_extra={"example": 1}
    )
    created_by_role: UserRoleEnum = Field(
        ..., description="建立者角色", json_schema_extra={"example": UserRoleEnum.TAKER}
    )


# class SchedulePartialUpdateRequest(BaseModel):
#     """部分更新時段的 API 請求模型。"""

#     schedule: ScheduleUpdateBase = Field(
#         ...,
#         description="要更新的時段資料",
#         json_schema_extra={
#             "example": {
#                 "giver_id": 1,
#                 "taker_id": 2,
#                 "status": "PENDING",
#                 "date": "2024-01-01",
#                 "start_time": "16:00:00",
#                 "end_time": "17:00:00",
#                 "note": "時段部分更新",
#             }
#         },
#     )
#     updated_by: int = Field(
#         ..., description="最後更新者的 ID", gt=0, json_schema_extra={"example": 1}
#     )
#     updated_by_role: UserRoleEnum = Field(
#         ...,
#         description="最後更新者的角色",
#         json_schema_extra={"example": UserRoleEnum.TAKER},
#     )


# class ScheduleDeleteRequest(BaseModel):
#     """刪除時段的 API 請求模型。"""

#     deleted_by: int = Field(
#         ..., description="刪除者的 ID", gt=0, json_schema_extra={"example": 1}
#     )
#     deleted_by_role: UserRoleEnum = Field(
#         ..., description="刪除者角色", json_schema_extra={"example": UserRoleEnum.TAKER}
#     )


# ===== 回應模型 =====
class ScheduleResponse(BaseModel):
    """時段回應模型。"""

    id: int = Field(..., description="時段 ID", gt=0, json_schema_extra={"example": 1})
    giver_id: int = Field(
        ..., description="Giver ID", gt=0, json_schema_extra={"example": 1}
    )
    taker_id: int | None = Field(
        None,
        description="Taker ID，可為 NULL（表示 Giver 提供時段供 Taker 預約）",
        gt=0,
        json_schema_extra={"example": 2},
    )
    status: ScheduleStatusEnum = Field(
        ...,
        description="時段狀態（後端會根據操作者角色自動決定：GIVER→AVAILABLE，TAKER→PENDING，其他→DRAFT）",
        json_schema_extra={"example": ScheduleStatusEnum.AVAILABLE},
    )
    schedule_date: date = Field(
        ...,
        description="時段日期",
        alias="date",
        json_schema_extra={"example": "2024-01-01"},
    )
    start_time: time = Field(
        ...,
        description="開始時間",
        json_schema_extra={"example": "09:00:00"},
    )
    end_time: time = Field(
        ...,
        description="結束時間",
        json_schema_extra={"example": "10:00:00"},
    )
    note: str | None = Field(
        None,
        description="備註",
        max_length=255,
        json_schema_extra={"example": "下週要面試，希望能請教面試技巧"},
    )
    created_at: datetime = Field(
        ...,
        description="建立時間（本地時間）",
        json_schema_extra={"example": "2024-01-01T09:00:00Z"},
    )
    created_by: int | None = Field(
        None,
        description="建立者的 ID，可為 NULL（表示系統自動建立）",
        gt=0,
        json_schema_extra={"example": 1},
    )
    created_by_role: UserRoleEnum = Field(
        ...,
        description="建立者角色",
        json_schema_extra={"example": UserRoleEnum.GIVER},
    )
    updated_at: datetime = Field(
        ...,
        description="更新時間（本地時間）",
        json_schema_extra={"example": "2024-01-01T09:00:00Z"},
    )
    updated_by: int | None = Field(
        None,
        description="最後更新者的 ID，可為 NULL（表示系統自動更新）",
        gt=0,
        json_schema_extra={"example": 1},
    )
    updated_by_role: UserRoleEnum = Field(
        ...,
        description="最後更新者角色",
        json_schema_extra={"example": UserRoleEnum.GIVER},
    )
    deleted_at: datetime | None = Field(
        None, description="軟刪除標記（本地時間）", json_schema_extra={"example": None}
    )
    deleted_by: int | None = Field(
        None,
        description="刪除者的 ID，可為 NULL（表示系統自動刪除）",
        gt=0,
        json_schema_extra={"example": None},
    )
    deleted_by_role: UserRoleEnum | None = Field(
        None, description="刪除者角色", json_schema_extra={"example": None}
    )

    model_config = ConfigDict(
        from_attributes=True,  # 允許 Pydantic 從 ORM 物件（而非 dict）的屬性中讀取資料，以進行驗證和序列化
        populate_by_name=True,  # 若欄位設定了別名，原欄位名稱、別名都能被正確解析
        extra="ignore",  # 當輸入資料包含模型未定義的欄位時，自動忽略，而非拋出驗證錯誤
    )

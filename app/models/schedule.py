"""時段資料模型。

定義時段資料表對應的 SQLAlchemy ORM 模型。
"""

# ===== 標準函式庫 =====
import logging
from typing import Any

# ===== 第三方套件 =====
from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    String,
    Time,
)
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

# ===== 本地模組 =====
from app.database import Base
from app.enums.models import ScheduleStatusEnum, UserRoleEnum
from app.utils.model_helpers import format_datetime, safe_getattr
from app.utils.timezone import get_local_now_naive


class Schedule(Base):  # type: ignore[misc,valid-type]
    """時段資料模型。"""

    __tablename__ = "schedules"

    # ===== 基本欄位 =====
    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        comment="時段 ID",
    )
    giver_id = Column(
        INTEGER(unsigned=True),
        ForeignKey(
            "users.id",
            ondelete="RESTRICT",
        ),  # 保護：不能刪除有時段的 Giver
        nullable=False,
        comment="Giver ID",
    )
    taker_id = Column(
        INTEGER(unsigned=True),
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),  # 靈活：Taker 刪除時設為 NULL（時段變可預約）
        nullable=True,
        comment="Taker ID，可為 NULL（表示 Giver 提供時段供 Taker 預約）",
    )
    status: "Column[ScheduleStatusEnum]" = Column(
        Enum(ScheduleStatusEnum),
        nullable=False,
        default=ScheduleStatusEnum.DRAFT,
        comment="時段狀態（後端會根據操作者角色自動決定：GIVER→AVAILABLE，TAKER→PENDING，其他→DRAFT）",
    )
    date = Column(
        Date,
        nullable=False,
        comment="時段日期",
    )
    start_time = Column(
        Time,
        nullable=False,
        comment="開始時間",
    )
    end_time = Column(
        Time,
        nullable=False,
        comment="結束時間",
    )
    note = Column(
        String(255),
        nullable=True,
        comment="備註",
    )

    # ===== 審計欄位 =====
    created_at = Column(
        DateTime,
        default=get_local_now_naive,
        nullable=False,
        comment="建立時間（本地時間）",
    )
    created_by = Column(
        INTEGER(unsigned=True),
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),  # 指向 users 表
        nullable=True,
        comment="建立者的 ID，可為 NULL（表示系統自動建立）",
    )
    created_by_role: "Column[UserRoleEnum]" = Column(
        Enum(UserRoleEnum),
        nullable=False,
        default=UserRoleEnum.SYSTEM,
        comment="建立者角色",
    )
    updated_at = Column(
        DateTime,
        default=get_local_now_naive,
        onupdate=get_local_now_naive,
        nullable=False,
        comment="更新時間（本地時間）",
    )
    updated_by = Column(
        INTEGER(unsigned=True),
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),  # 指向 users 表
        nullable=True,
        comment="最後更新者的 ID，可為 NULL（表示系統自動更新）",
    )
    updated_by_role: "Column[UserRoleEnum]" = Column(
        Enum(UserRoleEnum),
        nullable=False,
        default=UserRoleEnum.SYSTEM,
        comment="最後更新者角色",
    )

    # ===== 系統欄位 =====
    deleted_at = Column(
        DateTime,
        nullable=True,
        comment="軟刪除標記（本地時間）",
    )
    deleted_by = Column(
        INTEGER(unsigned=True),
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),  # 指向 users 表
        nullable=True,
        comment="刪除者的 ID，可為 NULL（表示系統自動刪除）",
    )
    deleted_by_role: "Column[UserRoleEnum]" = Column(
        Enum(UserRoleEnum),
        nullable=True,
        comment="刪除者角色，可為 NULL（未刪除時）",
    )

    # ===== 反向關聯 =====
    # 高頻使用 Eager loading 解決 N+1：使用 lazy="joined" 每次查詢都會載入所需關聯資料，避免多次查詢的 N+1 問題
    giver = relationship(
        "User",
        foreign_keys=[giver_id],
        back_populates="giver_schedules",
        lazy="joined",
    )
    taker = relationship(
        "User",
        foreign_keys=[taker_id],
        back_populates="taker_schedules",
        lazy="joined",
    )
    # 審計欄位低頻使用 Lazy loading：使用 lazy="select" 需要時再載入，避免不必要資料抓取
    created_by_user = relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_schedules",
        lazy="select",
    )
    updated_by_user = relationship(
        "User",
        foreign_keys=[updated_by],
        back_populates="updated_schedules",
        lazy="select",
    )
    deleted_by_user = relationship(
        "User",
        foreign_keys=[deleted_by],
        back_populates="deleted_schedules",
        lazy="select",
    )

    __table_args__ = (
        Index("idx_schedule_giver_date", "giver_id", "date", "start_time"),
        Index("idx_schedule_taker_date", "taker_id", "date", "start_time"),
        Index("idx_schedule_status", "status"),
        Index("idx_schedule_giver_time", "giver_id", "start_time", "end_time"),
    )

    @property
    def is_active(self) -> bool:
        """檢查記錄是否有效（未刪除）。"""
        return self.deleted_at is None

    @property
    def is_deleted(self) -> bool:
        """檢查記錄是否已刪除。"""
        return self.deleted_at is not None

    @property
    def is_available(self) -> bool:
        """檢查時段是否可預約。"""
        return bool(  # type: ignore
            self.is_active
            and self.status == ScheduleStatusEnum.AVAILABLE
            and self.taker_id is None
        )

    def __repr__(self) -> str:
        """字串表示。"""
        return (
            f"<Schedule(id={self.id}, giver_id={self.giver_id}, "
            f"date={self.date}, status={self.status})>"
        )

    def to_dict(self) -> dict[str, Any]:
        """資料序列化：轉換為字典格式，用於 API 和資料傳輸給前端。"""
        try:
            return {
                # 基本欄位：使用 getattr，避免不必要的 try/except
                "id": getattr(self, 'id', None),
                "giver_id": getattr(self, 'giver_id', None),
                "taker_id": getattr(self, 'taker_id', None),
                "status": getattr(self, 'status', None),
                "date": format_datetime(getattr(self, 'date', None)),
                "start_time": format_datetime(getattr(self, 'start_time', None)),
                "end_time": format_datetime(getattr(self, 'end_time', None)),
                "note": getattr(self, 'note', None),
                # 審計欄位
                "created_at": format_datetime(getattr(self, 'created_at', None)),
                "created_by": getattr(self, 'created_by', None),
                "created_by_role": getattr(self, 'created_by_role', None),
                "updated_at": format_datetime(getattr(self, 'updated_at', None)),
                "updated_by": getattr(self, 'updated_by', None),
                "updated_by_role": getattr(self, 'updated_by_role', None),
                # 系統欄位
                "deleted_at": format_datetime(getattr(self, 'deleted_at', None)),
                "deleted_by": getattr(self, 'deleted_by', None),
                "deleted_by_role": getattr(self, 'deleted_by_role', None),
                # ORM 關聯：使用 safe_getattr，避免 session 關閉等問題
                "created_by_user": (
                    safe_getattr(self, 'created_by_user').name
                    if safe_getattr(self, 'created_by_user')
                    else None
                ),
                "updated_by_user": (
                    safe_getattr(self, 'updated_by_user').name
                    if safe_getattr(self, 'updated_by_user')
                    else None
                ),
                "deleted_by_user": (
                    safe_getattr(self, 'deleted_by_user').name
                    if safe_getattr(self, 'deleted_by_user')
                    else None
                ),
                # 便利屬性
                "is_active": self.is_active,
                "is_deleted": self.is_deleted,
                "is_available": self.is_available,
            }
        except Exception as e:
            # 記錄錯誤但不中斷程式執行
            logger = logging.getLogger(__name__)
            logger.error(f"Schedule.to_dict() 錯誤: {e}", exc_info=True)

            # 返回基本資訊，避免 API 完全失敗
            return {
                "id": getattr(self, 'id', None),
                "giver_id": getattr(self, 'giver_id', None),
                "taker_id": getattr(self, 'taker_id', None),
                "status": getattr(self, 'status', ScheduleStatusEnum.DRAFT),
                "date": format_datetime(getattr(self, 'date', None)),
                "start_time": format_datetime(getattr(self, 'start_time', None)),
                "end_time": format_datetime(getattr(self, 'end_time', None)),
                "note": getattr(self, 'note', ''),
                "error": "資料序列化時發生錯誤",
            }

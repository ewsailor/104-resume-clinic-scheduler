"""使用者模型模組。

定義使用者資料表對應的 SQLAlchemy ORM 模型。
"""

# ===== 標準函式庫 =====
import logging
from typing import Any

# ===== 第三方套件 =====
from sqlalchemy import Column, DateTime, Index, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

# ===== 本地模組 =====
from app.database import Base
from app.utils.model_helpers import format_datetime
from app.utils.timezone import get_local_now_naive


class User(Base):  # type: ignore[misc,valid-type]
    """使用者資料表模型。"""

    __tablename__ = "users"

    # ===== 基本欄位 =====
    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        comment="使用者 ID",
    )
    name = Column(
        String(100),
        nullable=False,
        comment="使用者姓名",
    )
    email = Column(
        String(191),
        nullable=False,
        unique=True,
        comment="電子信箱（唯一）",
    )

    # ===== 審計欄位 =====
    created_at = Column(
        DateTime,
        default=get_local_now_naive,
        nullable=False,
        comment="建立時間（本地時間）",
    )
    updated_at = Column(
        DateTime,
        default=get_local_now_naive,
        onupdate=get_local_now_naive,
        nullable=False,
        comment="更新時間（本地時間）",
    )

    # ===== 系統欄位 =====
    deleted_at = Column(
        DateTime,
        nullable=True,
        comment="軟刪除標記（本地時間）",
    )

    # ===== 反向關聯 =====
    # 需要篩選：使用 lazy="dynamic"
    giver_schedules = relationship(
        "Schedule",
        foreign_keys="Schedule.giver_id",
        back_populates="giver",
        lazy="dynamic",
    )
    taker_schedules = relationship(
        "Schedule",
        foreign_keys="Schedule.taker_id",
        back_populates="taker",
        lazy="dynamic",
    )
    created_schedules = relationship(
        "Schedule",
        foreign_keys="Schedule.created_by",
        back_populates="created_by_user",
        lazy="dynamic",
    )
    updated_schedules = relationship(
        "Schedule",
        foreign_keys="Schedule.updated_by",
        back_populates="updated_by_user",
        lazy="dynamic",
    )
    deleted_schedules = relationship(
        "Schedule",
        foreign_keys="Schedule.deleted_by",
        back_populates="deleted_by_user",
        lazy="dynamic",
    )

    __table_args__ = (Index("idx_users_created_at", "created_at"),)

    @property
    def is_active(self) -> bool:
        """檢查記錄是否有效（未刪除）。"""
        return self.deleted_at is None

    @property
    def is_deleted(self) -> bool:
        """檢查記錄是否已刪除。"""
        return self.deleted_at is not None

    def __repr__(self) -> str:
        """字串表示，用於除錯和日誌。"""
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

    def to_dict(self) -> dict[str, Any]:
        """轉換為字典格式，用於 API 和資料傳輸給前端。"""
        try:
            return {
                # 基本欄位：使用 getattr，避免不必要的 try/except
                "id": getattr(self, 'id', None),
                "name": getattr(self, 'name', None),
                "email": getattr(self, 'email', None),
                "created_at": format_datetime(getattr(self, 'created_at', None)),
                "updated_at": format_datetime(getattr(self, 'updated_at', None)),
                "deleted_at": format_datetime(getattr(self, 'deleted_at', None)),
                # 便利屬性
                "is_active": self.is_active,
                "is_deleted": self.is_deleted,
            }
        except Exception as e:
            # 記錄錯誤但不中斷程式執行
            logger = logging.getLogger(__name__)
            logger.error(f"User.to_dict() 錯誤: {e}", exc_info=True)

            # 返回基本資訊，避免 API 完全失敗
            return {
                "id": getattr(self, 'id', None),
                "name": getattr(self, 'name', '未知'),
                "email": getattr(self, 'email', '未知'),
                "error": "資料序列化時發生錯誤",
            }

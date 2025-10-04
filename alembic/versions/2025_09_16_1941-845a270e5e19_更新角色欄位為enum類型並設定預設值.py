"""更新角色欄位為ENUM類型並設定預設值

Revision ID: 845a270e5e19
Revises: 0430aeaf5d1e
Create Date: 2025-09-16 19:41:20.474010

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '845a270e5e19'
down_revision: Union[str, Sequence[str], None] = '0430aeaf5d1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # 更新 created_by_role 欄位
    op.alter_column(
        'schedules',
        'created_by_role',
        existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM'),
        nullable=False,
        server_default='SYSTEM',
        comment='建立者角色',
    )

    # 更新 updated_by_role 欄位
    op.alter_column(
        'schedules',
        'updated_by_role',
        existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM'),
        nullable=False,
        server_default='SYSTEM',
        comment='最後更新者角色',
    )

    # 更新 deleted_by_role 欄位的註解
    op.alter_column(
        'schedules',
        'deleted_by_role',
        existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM'),
        nullable=True,
        comment='刪除者角色，可為 NULL（未刪除時）',
    )


def downgrade() -> None:
    """Downgrade schema."""
    # 恢復 created_by_role 欄位
    op.alter_column(
        'schedules',
        'created_by_role',
        existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM'),
        nullable=True,
        server_default=None,
        comment='建立者角色',
    )

    # 恢復 updated_by_role 欄位
    op.alter_column(
        'schedules',
        'updated_by_role',
        existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM'),
        nullable=True,
        server_default=None,
        comment='最後更新者角色',
    )

    # 恢復 deleted_by_role 欄位的註解
    op.alter_column(
        'schedules',
        'deleted_by_role',
        existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM'),
        nullable=True,
        comment='刪除者角色',
    )

"""新增updated_by_role欄位記錄更新者角色

Revision ID: 2dcbc8a2d77c
Revises: 5ddd0e85e3a2
Create Date: 2025-08-09 18:39:06.572944

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2dcbc8a2d77c'
down_revision: Union[str, Sequence[str], None] = '5ddd0e85e3a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # 新增 schedules 表格的 updated_by_role 欄位
    op.add_column(
        'schedules',
        sa.Column(
            'updated_by_role',
            sa.String(10),
            nullable=True,
            comment='最後更新者的角色：GIVER、TAKER 或 SYSTEM',
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    # 移除 schedules 表格的 updated_by_role 欄位
    op.drop_column('schedules', 'updated_by_role')

"""移除schedules表格中多餘的role欄位

Revision ID: a9ef819c8b8c
Revises: ff37a0caee1d
Create Date: 2025-08-09 20:24:59.741551

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a9ef819c8b8c'
down_revision: Union[str, Sequence[str], None] = 'ff37a0caee1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # 移除 schedules 表格中多餘的 role 欄位
    # 這個欄位與 updated_by_role 功能重複，且可以通過 giver_id/taker_id 判斷角色
    op.drop_column('schedules', 'role')


def downgrade() -> None:
    """Downgrade schema."""
    # 恢復 role 欄位（如果需要回滾）
    op.add_column(
        'schedules',
        sa.Column(
            'role',
            sa.String(10),
            nullable=False,
            server_default='GIVER',
            comment="角色：GIVER=提供者、TAKER=預約者",
        ),
    )

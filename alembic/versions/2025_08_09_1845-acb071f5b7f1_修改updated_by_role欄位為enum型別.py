"""修改updated_by_role欄位為ENUM型別

Revision ID: acb071f5b7f1
Revises: 2dcbc8a2d77c
Create Date: 2025-08-09 18:45:17.348489

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'acb071f5b7f1'
down_revision: Union[str, Sequence[str], None] = '2dcbc8a2d77c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # 建立 ENUM 型別
    user_role_enum = sa.Enum('GIVER', 'TAKER', 'SYSTEM', name='user_role_enum')
    user_role_enum.create(op.get_bind())

    # 修改 updated_by_role 欄位為 ENUM 型別
    with op.batch_alter_table('schedules') as batch_op:
        batch_op.alter_column(
            'updated_by_role',
            type_=user_role_enum,
            existing_type=sa.String(10),
            existing_nullable=True,
            existing_comment='最後更新者的角色：GIVER、TAKER 或 SYSTEM',
        )


def downgrade() -> None:
    """Downgrade schema."""
    # 改回 VARCHAR 型別
    with op.batch_alter_table('schedules') as batch_op:
        batch_op.alter_column(
            'updated_by_role',
            type_=sa.String(10),
            existing_type=sa.Enum('GIVER', 'TAKER', 'SYSTEM', name='user_role_enum'),
            existing_nullable=True,
            existing_comment='最後更新者的角色：GIVER、TAKER 或 SYSTEM',
        )

    # 刪除 ENUM 型別
    user_role_enum = sa.Enum('GIVER', 'TAKER', 'SYSTEM', name='user_role_enum')
    user_role_enum.drop(op.get_bind())

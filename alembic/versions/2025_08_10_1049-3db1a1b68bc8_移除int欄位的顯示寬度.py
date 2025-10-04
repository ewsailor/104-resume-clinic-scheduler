"""移除int欄位的顯示寬度

Revision ID: 3db1a1b68bc8
Revises: 32efeee7e8d4
Create Date: 2025-08-10 10:49:00.722604

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3db1a1b68bc8'
down_revision: Union[str, Sequence[str], None] = '32efeee7e8d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # 移除 users 表格中 int 欄位的顯示寬度
    # 使用 CHANGE COLUMN 來強制移除顯示寬度
    op.execute(
        "ALTER TABLE users CHANGE COLUMN id id int unsigned "
        "AUTO_INCREMENT COMMENT '使用者 ID'"
    )
    op.execute(
        "ALTER TABLE users CHANGE COLUMN updated_by updated_by int unsigned "
        "NULL COMMENT '最後更新者的使用者 ID，可為 NULL（表示系統自動更新）'"
    )

    # 移除 schedules 表格中 int 欄位的顯示寬度（如果存在）
    op.execute("ALTER TABLE schedules CHANGE COLUMN id id int unsigned AUTO_INCREMENT")
    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN giver_id giver_id int unsigned NOT NULL"
    )
    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN taker_id taker_id int unsigned NULL"
    )
    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN updated_by updated_by int unsigned NULL"
    )


def downgrade() -> None:
    """Downgrade schema."""
    # 恢復顯示寬度（如果需要回滾）
    op.execute("ALTER TABLE users CHANGE COLUMN id id int(10) unsigned AUTO_INCREMENT")
    op.execute(
        "ALTER TABLE users CHANGE COLUMN updated_by updated_by int(10) unsigned NULL"
    )

    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN id id int(10) unsigned AUTO_INCREMENT"
    )
    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN giver_id giver_id "
        "int(10) unsigned NOT NULL"
    )
    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN taker_id taker_id " "int(10) unsigned NULL"
    )
    op.execute(
        "ALTER TABLE schedules CHANGE COLUMN updated_by updated_by "
        "int(10) unsigned NULL"
    )

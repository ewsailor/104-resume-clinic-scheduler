"""設定_sql_mode_嚴格模式

Revision ID: 0430aeaf5d1e
Revises: 985e30da6e53
Create Date: 2025-08-23 01:35:07.618524

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '0430aeaf5d1e'
down_revision: Union[str, Sequence[str], None] = '985e30da6e53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    設定 MySQL sql_mode 為嚴格模式。

    嚴格模式包含：
    - STRICT_TRANS_TABLES: 事務性表格的嚴格模式
    - NO_ZERO_DATE: 不允許零日期
    - NO_ZERO_IN_DATE: 不允許日期中的零值
    - ERROR_FOR_DIVISION_BY_ZERO: 除零錯誤
    """
    # 設定全域 sql_mode 為嚴格模式
    # 注意：這需要 SUPER 權限才能設定全域變數
    op.execute(
        "SET GLOBAL sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'"
    )

    # 同時設定會話級別的 sql_mode
    op.execute(
        "SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'"
    )


def downgrade() -> None:
    """
    恢復 sql_mode 為預設值。

    將 sql_mode 設為 MySQL 的預設值，移除嚴格模式限制。
    """
    # 恢復全域 sql_mode 為預設值
    op.execute("SET GLOBAL sql_mode = ''")

    # 恢復會話級別的 sql_mode
    op.execute("SET SESSION sql_mode = ''")

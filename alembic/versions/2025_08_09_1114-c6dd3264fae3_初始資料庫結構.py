"""初始資料庫結構

Revision ID: c6dd3264fae3
Revises:
Create Date: 2025-08-09 11:14:15.156596

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = 'c6dd3264fae3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""

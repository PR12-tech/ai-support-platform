"""remove conversation messages table

Revision ID: 5e21d3d54777
Revises: 39141d88599c
Create Date: 2026-08-13 19:59:02.566590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e21d3d54777'
down_revision: Union[str, Sequence[str], None] = '39141d88599c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.drop_table("conversation_messages")


def downgrade() -> None:
    """Downgrade schema."""
    pass

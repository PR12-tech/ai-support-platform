"""allow optional ticket assignment

Revision ID: 39141d88599c
Revises: b863a4b8f84c
Create Date: 2026-08-13 16:11:18.142634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39141d88599c'
down_revision: Union[str, Sequence[str], None] = 'b863a4b8f84c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.alter_column(
        "tickets",
        "priority",
        existing_type=sa.String(),
        nullable=True
    )

    op.alter_column(
        "tickets",
        "assigned_to",
        existing_type=sa.String(),
        nullable=True
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column(
        "tickets",
        "priority",
        existing_type=sa.String(),
        nullable=False
    )

    op.alter_column(
        "tickets",
        "assigned_to",
        existing_type=sa.String(),
        nullable=False
    )

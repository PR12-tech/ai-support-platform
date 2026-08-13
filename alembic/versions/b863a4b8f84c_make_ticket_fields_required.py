"""make ticket fields required

Revision ID: b863a4b8f84c
Revises: 45ded6e7a192
Create Date: 2026-08-13 15:34:23.263547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b863a4b8f84c'
down_revision: Union[str, Sequence[str], None] = '45ded6e7a192'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.alter_column(
        "tickets",
        "ticket_id",
        existing_type=sa.String(),
        nullable=False
    )

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


def downgrade() -> None:
    """Downgrade schema."""
    pass

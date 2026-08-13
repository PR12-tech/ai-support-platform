"""add unified ticket fields

Revision ID: efd9baea33a7
Revises: 667cae9061f5
Create Date: 2026-08-13 11:55:44.479021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'efd9baea33a7'
down_revision: Union[str, Sequence[str], None] = '667cae9061f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "tickets",
        sa.Column(
            "ticket_id",
            sa.String(),
            nullable=True
        )
    )

    op.add_column(
        "tickets",
        sa.Column(
            "priority",
            sa.String(),
            nullable=True
        )
    )

    op.add_column(
        "tickets",
        sa.Column(
            "assigned_to",
            sa.String(),
            nullable=True
        )
    )

    op.create_unique_constraint(
        "uq_tickets_ticket_id",
        "tickets",
        ["ticket_id"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass

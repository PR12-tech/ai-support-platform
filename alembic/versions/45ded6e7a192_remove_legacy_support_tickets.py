"""remove legacy support tickets

Revision ID: 45ded6e7a192
Revises: efd9baea33a7
Create Date: 2026-08-13 13:11:53.604134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45ded6e7a192'
down_revision: Union[str, Sequence[str], None] = 'efd9baea33a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.drop_table("support_tickets")


def downgrade() -> None:
    """Downgrade schema."""

    op.create_table(
        "support_tickets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ticket_id", sa.String(), nullable=False),
        sa.Column("customer", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("priority", sa.String(), nullable=False),
        sa.Column("assigned_to", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ticket_id")
    )

    op.create_index(
        "ix_support_tickets_id",
        "support_tickets",
        ["id"],
        unique=False
    )

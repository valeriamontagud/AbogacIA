"""add role to users

Revision ID: c08101c6903f
Revises: b7edd5177850
Create Date: 2026-05-27 15:01:09.314090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c08101c6903f'
down_revision: Union[str, Sequence[str], None] = 'b7edd5177850'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "role",
            sa.String(),
            nullable=False,
            server_default="lawyer",
        ),
    )
    op.alter_column(
        "users",
        "role",
        server_default=None,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "role")

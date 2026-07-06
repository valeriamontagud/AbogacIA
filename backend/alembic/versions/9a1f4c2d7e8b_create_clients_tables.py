"""create clients tables

Revision ID: 9a1f4c2d7e8b
Revises: c08101c6903f
Create Date: 2026-07-06 20:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9a1f4c2d7e8b"
down_revision: Union[str, Sequence[str], None] = "c08101c6903f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "clients",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("dni", sa.String(), nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.Column("accident_date", sa.Date(), nullable=True),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("data_source", sa.String(), nullable=False),
        sa.Column("created_by_user_id", sa.Uuid(as_uuid=False), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["created_by_user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("dni"),
    )
    op.create_index(
        op.f("ix_clients_created_by_user_id"),
        "clients",
        ["created_by_user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_clients_dni"),
        "clients",
        ["dni"],
        unique=False,
    )
    op.create_index(
        op.f("ix_clients_full_name"),
        "clients",
        ["full_name"],
        unique=False,
    )

    op.create_table(
        "client_documents",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("client_id", sa.String(length=36), nullable=False),
        sa.Column("original_filename", sa.String(), nullable=False),
        sa.Column("stored_filename", sa.String(), nullable=False),
        sa.Column("storage_path", sa.String(), nullable=False),
        sa.Column("content_type", sa.String(), nullable=True),
        sa.Column("size_bytes", sa.BigInteger(), nullable=False),
        sa.Column("uploaded_by_user_id", sa.Uuid(as_uuid=False), nullable=False),
        sa.Column("source", sa.String(), nullable=False),
        sa.Column("ai_processing_status", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["clients.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(["uploaded_by_user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_client_documents_client_id"),
        "client_documents",
        ["client_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_client_documents_uploaded_by_user_id"),
        "client_documents",
        ["uploaded_by_user_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_client_documents_uploaded_by_user_id"),
        table_name="client_documents",
    )
    op.drop_index(
        op.f("ix_client_documents_client_id"),
        table_name="client_documents",
    )
    op.drop_table("client_documents")

    op.drop_index(
        op.f("ix_clients_full_name"),
        table_name="clients",
    )
    op.drop_index(
        op.f("ix_clients_dni"),
        table_name="clients",
    )
    op.drop_index(
        op.f("ix_clients_created_by_user_id"),
        table_name="clients",
    )
    op.drop_table("clients")

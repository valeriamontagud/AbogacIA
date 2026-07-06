import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    BigInteger,
    Column,
    Date,
    DateTime,
    ForeignKey,
    String,
    Text,
    Uuid,
)
from sqlalchemy.orm import relationship

from app.database.base import Base


def utc_now():
    return datetime.now(timezone.utc)


class Client(Base):

    __tablename__ = "clients"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    full_name = Column(
        String,
        nullable=False,
        index=True
    )

    dni = Column(
        String,
        unique=True,
        nullable=True,
        index=True
    )

    birth_date = Column(
        Date,
        nullable=True
    )

    accident_date = Column(
        Date,
        nullable=True
    )

    address = Column(
        Text,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    email = Column(
        String,
        nullable=True
    )

    notes = Column(
        Text,
        nullable=True
    )

    data_source = Column(
        String,
        default="manual",
        nullable=False
    )

    created_by_user_id = Column(
        Uuid(as_uuid=False),
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    created_at = Column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False
    )

    documents = relationship(
        "ClientDocument",
        back_populates="client",
        cascade="all, delete-orphan"
    )


class ClientDocument(Base):

    __tablename__ = "client_documents"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    client_id = Column(
        String(36),
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    original_filename = Column(
        String,
        nullable=False
    )

    stored_filename = Column(
        String,
        nullable=False
    )

    storage_path = Column(
        String,
        nullable=False
    )

    content_type = Column(
        String,
        nullable=True
    )

    size_bytes = Column(
        BigInteger,
        nullable=False
    )

    uploaded_by_user_id = Column(
        Uuid(as_uuid=False),
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    source = Column(
        String,
        default="manual",
        nullable=False
    )

    ai_processing_status = Column(
        String,
        default="not_requested",
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False
    )

    client = relationship(
        "Client",
        back_populates="documents"
    )

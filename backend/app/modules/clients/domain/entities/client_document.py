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
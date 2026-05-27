import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    full_name = Column(
        String,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    # =====================================================
    # Rol usuario
    # =====================================================

    role = Column(
        String,
        default="lawyer",
        nullable=False
    )
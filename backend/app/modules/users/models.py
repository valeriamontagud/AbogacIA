import uuid

from sqlalchemy import Column, String
from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    # Usar String genérico para compatibilidad con SQLite en pruebas.
    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
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
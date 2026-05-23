"""
Configuración sesión SQLAlchemy.

Responsable de:
- engine DB
- SessionLocal
- dependency get_db
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings


# ---------------------------------------------------------
# Crear engine SQLAlchemy
# ---------------------------------------------------------
# Engine = conexión principal PostgreSQL
# ---------------------------------------------------------

engine = create_engine(
    settings.DATABASE_URL
)


# ---------------------------------------------------------
# Session factory
# ---------------------------------------------------------
# Cada request tendrá su propia sesión DB.
# ---------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ---------------------------------------------------------
# Dependency FastAPI
# ---------------------------------------------------------
# FastAPI:
#
# request
# ↓
# crea sesión
# ↓
# yield db
# ↓
# cierra sesión
# ---------------------------------------------------------

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
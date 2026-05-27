"""Configuración compartida de tests.

Este archivo prepara un entorno de pruebas estable para la aplicación.
Usa SQLite en memoria y sobrescribe la dependencia de FastAPI para no tocar la DB real.
"""

import os

# Establecer variables de entorno necesarias antes de importar la aplicación.
os.environ.setdefault("APP_NAME", "AbogacIA")
os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("API_V1_STR", "/api/v1")
os.environ.setdefault("SECRET_KEY", "TEST_SECRET_KEY")
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
os.environ.setdefault("POSTGRES_SERVER", "localhost")
os.environ.setdefault("POSTGRES_USER", "user")
os.environ.setdefault("POSTGRES_PASSWORD", "password")
os.environ.setdefault("POSTGRES_DB", "testdb")

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.database.session import get_db as get_db_dependency
from app.modules.users.models import User
from app.main import app

# Usar una base de datos SQLite en memoria con StaticPool para compartir la misma conexión.
engine = create_engine(
    os.environ["DATABASE_URL"],
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    """Reemplaza la dependencia get_db de la app por la versión de prueba."""

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db_dependency] = override_get_db


def client():
@pytest.fixture(scope="session")
def client():
    """Cliente HTTP de pruebas para llamar endpoints de la app."""

    return TestClient(app)


def db():
@pytest.fixture(scope="function")
def db():
    """Session transaccional para pruebas de base de datos.

    Al finalizar cada prueba se hace rollback para mantener la base limpia.
    """

    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def clear_users(db):
@pytest.fixture(autouse=True)
def clear_users(db):
    """Borra todos los usuarios antes de cada prueba para evitar efectos secundarios."""

    db.query(User).delete()
    db.commit()

"""Tests del servicio de autenticación.

Verifican registro, login y manejo de errores de usuario duplicado o credenciales inválidas.
"""

import pytest

from app.modules.auth.service import AuthService
from app.shared.exceptions.exceptions import BadRequestException, UnauthorizedException
from app.modules.users.models import User


def test_register_creates_user(db):
    # Registrar un usuario nuevo usando el servicio.
    service = AuthService()

    user = service.register(
        db,
        "testuser@example.com",
        "password123",
        "Test User"
    )

    assert user.email == "testuser@example.com"
    assert user.full_name == "Test User"
    assert user.hashed_password != "password123"
    assert db.query(User).filter(User.email == "testuser@example.com").first() is not None


def test_register_duplicate_email_raises_bad_request(db):
    service = AuthService()

    service.register(
        db,
        "duplicate@example.com",
        "password123",
        "Duplicate"
    )

    with pytest.raises(BadRequestException):
        service.register(
            db,
            "duplicate@example.com",
            "password123",
            "Duplicate"
        )


def test_login_returns_access_token(db):
    service = AuthService()

    service.register(
        db,
        "login@example.com",
        "password123",
        "Login User"
    )

    result = service.login(db, "login@example.com", "password123")

    assert "access_token" in result
    assert result["access_token"]


def test_login_invalid_credentials_raises_unauthorized(db):
    service = AuthService()

    with pytest.raises(UnauthorizedException):
        service.login(db, "missing@example.com", "password123")

    service.register(
        db,
        "wrongpass@example.com",
        "password123",
        "Wrong Pass"
    )

    with pytest.raises(UnauthorizedException):
        service.login(db, "wrongpass@example.com", "badpassword")

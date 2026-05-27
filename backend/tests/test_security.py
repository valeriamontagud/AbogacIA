"""Tests unitarios de seguridad.

Comprueban el hash de contraseñas y la generación/validación de JWT.
"""

from app.shared.security.hashing import hash_password, verify_password
from app.shared.security.jwt import create_access_token, decode_access_token


def test_hash_password_and_verify_password():
    # password original
    password = "Secret123!"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("WrongPassword", hashed)


def test_create_and_decode_access_token():
    payload = {"sub": "1234"}
    token = create_access_token(payload)

    decoded = decode_access_token(token)

    assert decoded is not None
    assert decoded["sub"] == "1234"
    assert "exp" in decoded

    assert decode_access_token("invalid.token.value") is None

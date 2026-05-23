"""
Servicio autenticación.

Responsable de:
- register
- login
- validaciones auth
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.users.repository import UserRepository

from app.shared.security.hashing import (
    hash_password,
    verify_password
)

from app.shared.security.jwt import (
    create_access_token
)

from app.modules.users.models import User


class AuthService:

    def __init__(self):

        self.user_repository = UserRepository()

    # ---------------------------------------------------------
    # Register
    # ---------------------------------------------------------

    def register(
        self,
        db: Session,
        email: str,
        password: str,
        full_name: str
    ):

        # ---------------------------------------------------------
        # Verificar email existente
        # ---------------------------------------------------------

        existing_user = (
            self.user_repository.get_by_email(
                db,
                email
            )
        )

        if existing_user:

            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        # ---------------------------------------------------------
        # Hash password
        # ---------------------------------------------------------
        print(password)
        print(type(password))
        hashed_password = hash_password(password)

        # ---------------------------------------------------------
        # Crear usuario
        # ---------------------------------------------------------

        user = self.user_repository.create(
            db,
            {
                "email": email,
                "full_name": full_name,
                "hashed_password": hashed_password
            }
        )

        return user

    # ---------------------------------------------------------
    # Login
    # ---------------------------------------------------------

    def login(
        self,
        db: Session,
        email: str,
        password: str
    ):

        # ---------------------------------------------------------
        # Buscar usuario
        # ---------------------------------------------------------

        user = self.user_repository.get_by_email(
            db,
            email
        )

        if not user:

            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        # ---------------------------------------------------------
        # Validar password
        # ---------------------------------------------------------

        is_valid = verify_password(
            password,
            user.hashed_password
        )

        if not is_valid:

            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        # ---------------------------------------------------------
        # Crear JWT
        # ---------------------------------------------------------

        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": access_token
        }
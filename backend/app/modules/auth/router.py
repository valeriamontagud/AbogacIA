"""
Router auth.

Expone endpoints HTTP auth.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.users.models import User

from app.modules.auth.dependencies import get_current_user

from app.modules.auth.schemas import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from app.modules.auth.service import AuthService
from fastapi.security import OAuth2PasswordRequestForm

# =========================================================
# Router config
# =========================================================

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

auth_service = AuthService()


# =========================================================
# Register
# =========================================================

@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    """
    Registrar nuevo usuario.
    """

    user = auth_service.register(
        db,
        data.email,
        data.password,
        data.full_name
    )

    return {
        "id": str(user.id),
        "email": user.email
    }


# =========================================================
# Login
# =========================================================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Login usuario.
    Devuelve JWT token.
    """

    return auth_service.login(
        db,
        form_data.username,
        form_data.password
    )


# =========================================================
# Current authenticated user
# =========================================================

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    """
    Obtener usuario autenticado actual.
    Ruta protegida con JWT.
    """

    return {
        "id": str(current_user.id),
        "email": current_user.email,
        "full_name": current_user.full_name
    }
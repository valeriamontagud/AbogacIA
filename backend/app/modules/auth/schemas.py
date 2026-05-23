"""
Schemas del módulo auth.

Responsables de:
- validar requests
- validar responses
"""

from pydantic import BaseModel, EmailStr


# ---------------------------------------------------------
# Register request
# ---------------------------------------------------------

class RegisterRequest(BaseModel):

    email: EmailStr

    password: str

    full_name: str


# ---------------------------------------------------------
# Login request
# ---------------------------------------------------------

class LoginRequest(BaseModel):

    email: EmailStr

    password: str


# ---------------------------------------------------------
# Auth response
# ---------------------------------------------------------

class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"
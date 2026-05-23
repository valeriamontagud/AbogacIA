"""
Configuración de autenticación.

Separar settings por contexto es arquitectura enterprise.
"""

from pydantic_settings import BaseSettings


class AuthSettings(BaseSettings):

    # ---------------------------------------------------------
    # Secret key JWT
    # ---------------------------------------------------------
    # En producción irá en variables entorno.
    # ---------------------------------------------------------
    
    #Cambiar esto cuando este en producción, no debe estar aqui tendra que estar en el env.
    AUTH_SECRET_KEY: str = (
        "SUPER_SECRET_KEY"
    )

    # ---------------------------------------------------------
    # Algoritmo JWT
    # ---------------------------------------------------------

    AUTH_ALGORITHM: str = "HS256"

    # ---------------------------------------------------------
    # Expiración token
    # ---------------------------------------------------------

    AUTH_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


auth_settings = AuthSettings()
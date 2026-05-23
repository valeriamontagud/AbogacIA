from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt


# CLAVE SECRETA
# En producción irá en .env ESTO VA EN EL ENV EN PRODUCCIÓN
SECRET_KEY = "SUPER_SECRET_KEY"

# Algoritmo JWT
ALGORITHM = "HS256"

# Tiempo expiración token
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict) -> str:
    """
    Crear JWT token firmado.
    """

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Validar y decodificar JWT.
    """

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None
"""
Funciones de seguridad para:
- hashear passwords
- verificar passwords

Nunca guardamos passwords en texto plano.
"""

from passlib.context import CryptContext


# ---------------------------------------------------------
# Contexto criptográfico global
# ---------------------------------------------------------
# bcrypt es el estándar moderno para passwords.
# ---------------------------------------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ---------------------------------------------------------
# Generar hash password
# ---------------------------------------------------------
# Convierte:
#
# 123456
#
# en:
#
# $2b$12$asdasdas...
# ---------------------------------------------------------

def hash_password(password: str) -> str:

    return pwd_context.hash(password)


# ---------------------------------------------------------
# Verificar password
# ---------------------------------------------------------
# Compara:
#
# password login
#
# VS
#
# hash almacenado DB
# ---------------------------------------------------------

#Siempre se debe usar esta función para verificar passwords, nunca comparar el hash directamente.
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password
    )
"""
Repositorio usuarios.

Responsable de:
- acceso a base de datos
- queries SQLAlchemy
"""

from sqlalchemy.orm import Session

from app.modules.users.models import User


class UserRepository:

    # ---------------------------------------------------------
    # Obtener usuario por email
    # ---------------------------------------------------------

    def get_by_email(
        self,
        db: Session,
        email: str
    ):

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    # ---------------------------------------------------------
    # Crear usuario
    # ---------------------------------------------------------

    def create(
        self,
        db: Session,
        user_data: dict
    ):

        user = User(**user_data)

        db.add(user)

        db.commit()

        db.refresh(user)

        return user
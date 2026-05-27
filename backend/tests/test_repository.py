"""Test del repositorio de usuarios.

Valida la creación y recuperación de usuarios en la base de datos.
"""

from app.modules.users.repository import UserRepository


def test_user_repository_create_and_get_by_email(db):
    repository = UserRepository()

    repository.create(
        db,
        {
            "email": "repo@example.com",
            "full_name": "Repo User",
            "hashed_password": "hash123"
        }
    )

    user = repository.get_by_email(db, "repo@example.com")

    assert user is not None
    assert user.email == "repo@example.com"
    assert user.full_name == "Repo User"

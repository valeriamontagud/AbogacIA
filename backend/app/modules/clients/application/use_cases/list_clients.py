from sqlalchemy.orm import Session

from app.modules.clients.domain.entities import Client
from app.modules.clients.infrastructure.persistence import (
    SQLAlchemyClientRepository,
)


class ListClientsUseCase:

    def __init__(self):

        self.repository = SQLAlchemyClientRepository()

    def execute(
        self,
        db: Session,
        user_id: str
    ) -> list[Client]:

        return self.repository.list_by_user(
            db,
            user_id
        )
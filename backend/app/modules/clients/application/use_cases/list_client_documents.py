from sqlalchemy.orm import Session

from app.modules.clients.domain.entities import ClientDocument
from app.modules.clients.infrastructure.persistence import (
    SQLAlchemyClientRepository,
)
from app.shared.exceptions.exceptions import (
    NotFoundException,
)


class ListDocumentsUseCase:

    def __init__(self):

        self.repository = SQLAlchemyClientRepository()

    def execute(
        self,
        db: Session,
        client_id: str,
        user_id: str,
    ) -> list[ClientDocument]:

        client = self.repository.get_by_id(
            db,
            client_id,
            user_id,
        )

        if not client:
            raise NotFoundException(
                "Client not found"
            )

        return self.repository.list_documents(
            db,
            client_id,
        )
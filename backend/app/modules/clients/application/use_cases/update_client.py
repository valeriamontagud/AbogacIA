from sqlalchemy.orm import Session

from app.modules.clients.domain.entities import Client
from app.modules.clients.infrastructure.persistence import (
    SQLAlchemyClientRepository,
)
from app.modules.clients.presentation.schemas import ClientUpdate
from app.shared.exceptions.exceptions import (
    BadRequestException,
    NotFoundException,
)


class UpdateClientUseCase:

    def __init__(self):

        self.repository = SQLAlchemyClientRepository()

    def execute(
        self,
        db: Session,
        client_id: str,
        data: ClientUpdate,
        user_id: str,
    ) -> Client:

        client = self.repository.get_by_id(
            db,
            client_id,
            user_id,
        )

        if not client:
            raise NotFoundException(
                "Client not found"
            )

        update_data = data.model_dump(
            exclude_unset=True
        )

        if (
            "dni" in update_data
            and update_data["dni"]
        ):

            existing = self.repository.get_by_dni(
                db,
                update_data["dni"],
            )

            if existing and existing.id != client.id:
                raise BadRequestException(
                    "Client with this DNI already exists"
                )

        return self.repository.update(
            db,
            client,
            update_data,
        )
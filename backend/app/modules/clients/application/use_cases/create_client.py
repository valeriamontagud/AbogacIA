from sqlalchemy.orm import Session

from app.modules.clients.domain.entities import Client
from app.modules.clients.infrastructure.persistence import (
    SQLAlchemyClientRepository,
)
from app.modules.clients.presentation.schemas import ClientCreate
from app.shared.exceptions.exceptions import BadRequestException


class CreateClientUseCase:

    def __init__(self):

        self.repository = SQLAlchemyClientRepository()

    def execute(
        self,
        db: Session,
        data: ClientCreate,
        user_id: str
    ) -> Client:

        if data.dni:

            existing = self.repository.get_by_dni(
                db,
                data.dni
            )

            if existing:

                raise BadRequestException(
                    "Client with this DNI already exists"
                )

        return self.repository.create(
            db,
            {
                **data.model_dump(),
                "created_by_user_id": user_id,
                "data_source": "manual",
            }
        )
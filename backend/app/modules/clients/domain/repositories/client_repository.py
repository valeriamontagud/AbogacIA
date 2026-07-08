from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.modules.clients.domain.entities import (
    Client,
    ClientDocument,
)


class ClientRepository(ABC):

    @abstractmethod
    def create(
        self,
        db: Session,
        client_data: dict
    ) -> Client:
        pass

    @abstractmethod
    def list_by_user(
        self,
        db: Session,
        created_by_user_id: str
    ) -> list[Client]:
        pass

    @abstractmethod
    def get_by_id(
        self,
        db: Session,
        client_id: str,
        created_by_user_id: str
    ) -> Client | None:
        pass

    @abstractmethod
    def get_by_dni(
        self,
        db: Session,
        dni: str
    ) -> Client | None:
        pass

    @abstractmethod
    def update(
        self,
        db: Session,
        client: Client,
        client_data: dict
    ) -> Client:
        pass

    @abstractmethod
    def add_document(
        self,
        db: Session,
        document_data: dict
    ) -> ClientDocument:
        pass

    @abstractmethod
    def list_documents(
        self,
        db: Session,
        client_id: str
    ) -> list[ClientDocument]:
        pass
from sqlalchemy.orm import Session

from app.modules.clients.models import Client, ClientDocument


class ClientRepository:

    def create(
        self,
        db: Session,
        client_data: dict
    ) -> Client:

        client = Client(**client_data)

        db.add(client)
        db.commit()
        db.refresh(client)

        return client

    def list_by_user(
        self,
        db: Session,
        created_by_user_id: str
    ) -> list[Client]:

        return (
            db.query(Client)
            .filter(Client.created_by_user_id == created_by_user_id)
            .order_by(Client.created_at.desc())
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        client_id: str,
        created_by_user_id: str
    ) -> Client | None:

        return (
            db.query(Client)
            .filter(Client.id == client_id)
            .filter(Client.created_by_user_id == created_by_user_id)
            .first()
        )

    def get_by_dni(
        self,
        db: Session,
        dni: str
    ) -> Client | None:

        return (
            db.query(Client)
            .filter(Client.dni == dni)
            .first()
        )

    def update(
        self,
        db: Session,
        client: Client,
        client_data: dict
    ) -> Client:

        for key, value in client_data.items():
            setattr(client, key, value)

        db.commit()
        db.refresh(client)

        return client

    def add_document(
        self,
        db: Session,
        document_data: dict
    ) -> ClientDocument:

        document = ClientDocument(**document_data)

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    def list_documents(
        self,
        db: Session,
        client_id: str
    ) -> list[ClientDocument]:

        return (
            db.query(ClientDocument)
            .filter(ClientDocument.client_id == client_id)
            .order_by(ClientDocument.created_at.desc())
            .all()
        )

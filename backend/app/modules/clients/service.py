from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.modules.clients.models import Client, ClientDocument
from app.modules.clients.repository import ClientRepository
from app.modules.clients.schemas import ClientCreate, ClientUpdate
from app.shared.exceptions.exceptions import BadRequestException, NotFoundException


class ClientService:

    def __init__(self):

        self.client_repository = ClientRepository()
        self.upload_root = Path("storage/uploads/clients")

    def create_client(
        self,
        db: Session,
        data: ClientCreate,
        user_id: str
    ) -> Client:

        if data.dni:
            existing_client = self.client_repository.get_by_dni(
                db,
                data.dni
            )

            if existing_client:
                raise BadRequestException(
                    "Client with this DNI already exists"
                )

        return self.client_repository.create(
            db,
            {
                **data.model_dump(),
                "created_by_user_id": user_id,
                "data_source": "manual",
            }
        )

    def list_clients(
        self,
        db: Session,
        user_id: str
    ) -> list[Client]:

        return self.client_repository.list_by_user(
            db,
            user_id
        )

    def get_client(
        self,
        db: Session,
        client_id: str,
        user_id: str
    ) -> Client:

        client = self.client_repository.get_by_id(
            db,
            client_id,
            user_id
        )

        if not client:
            raise NotFoundException("Client not found")

        return client

    def update_client(
        self,
        db: Session,
        client_id: str,
        data: ClientUpdate,
        user_id: str
    ) -> Client:

        client = self.get_client(
            db,
            client_id,
            user_id
        )

        update_data = data.model_dump(
            exclude_unset=True
        )

        if "dni" in update_data and update_data["dni"]:
            existing_client = self.client_repository.get_by_dni(
                db,
                update_data["dni"]
            )

            if existing_client and existing_client.id != client.id:
                raise BadRequestException(
                    "Client with this DNI already exists"
                )

        return self.client_repository.update(
            db,
            client,
            update_data
        )

    def upload_document(
        self,
        db: Session,
        client_id: str,
        file: UploadFile,
        user_id: str
    ) -> ClientDocument:

        self.get_client(
            db,
            client_id,
            user_id
        )

        original_filename = file.filename or "document"
        suffix = Path(original_filename).suffix
        stored_filename = f"{uuid4()}{suffix}"
        client_directory = self.upload_root / client_id
        storage_path = client_directory / stored_filename

        client_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        size_bytes = 0

        with storage_path.open("wb") as destination:
            while chunk := file.file.read(1024 * 1024):
                size_bytes += len(chunk)
                destination.write(chunk)

        return self.client_repository.add_document(
            db,
            {
                "client_id": client_id,
                "original_filename": original_filename,
                "stored_filename": stored_filename,
                "storage_path": str(storage_path),
                "content_type": file.content_type,
                "size_bytes": size_bytes,
                "uploaded_by_user_id": user_id,
                "source": "manual",
                "ai_processing_status": "not_requested",
            }
        )

    def list_documents(
        self,
        db: Session,
        client_id: str,
        user_id: str
    ) -> list[ClientDocument]:

        self.get_client(
            db,
            client_id,
            user_id
        )

        return self.client_repository.list_documents(
            db,
            client_id
        )

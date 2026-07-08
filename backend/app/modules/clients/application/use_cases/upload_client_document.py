from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.modules.clients.domain.entities import ClientDocument
from app.modules.clients.infrastructure.persistence import (
    SQLAlchemyClientRepository,
)
from app.shared.exceptions.exceptions import (
    NotFoundException,
)


class UploadDocumentUseCase:

    def __init__(self):

        self.repository = SQLAlchemyClientRepository()
        self.upload_root = Path("storage/uploads/clients")

    def execute(
        self,
        db: Session,
        client_id: str,
        file: UploadFile,
        user_id: str,
    ) -> ClientDocument:

        client = self.repository.get_by_id(
            db,
            client_id,
            user_id,
        )

        if not client:
            raise NotFoundException(
                "Client not found"
            )

        original_filename = file.filename or "document"

        suffix = Path(
            original_filename
        ).suffix

        stored_filename = (
            f"{uuid4()}{suffix}"
        )

        client_directory = (
            self.upload_root / client_id
        )

        storage_path = (
            client_directory / stored_filename
        )

        client_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        size_bytes = 0

        with storage_path.open("wb") as destination:

            while chunk := file.file.read(
                1024 * 1024
            ):

                size_bytes += len(chunk)

                destination.write(chunk)

        return self.repository.add_document(
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
            },
        )
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.clients.schemas import (
    ClientCreate,
    ClientDocumentResponse,
    ClientResponse,
    ClientUpdate,
)
from app.modules.clients.service import ClientService
from app.modules.users.models import User


router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

client_service = ClientService()


@router.post(
    "",
    response_model=ClientResponse
)
def create_client(
    data: ClientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return client_service.create_client(
        db,
        data,
        str(current_user.id)
    )


@router.get(
    "",
    response_model=list[ClientResponse]
)
def list_clients(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return client_service.list_clients(
        db,
        str(current_user.id)
    )


@router.get(
    "/{client_id}",
    response_model=ClientResponse
)
def get_client(
    client_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return client_service.get_client(
        db,
        client_id,
        str(current_user.id)
    )


@router.patch(
    "/{client_id}",
    response_model=ClientResponse
)
def update_client(
    client_id: str,
    data: ClientUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return client_service.update_client(
        db,
        client_id,
        data,
        str(current_user.id)
    )


@router.post(
    "/{client_id}/documents",
    response_model=ClientDocumentResponse
)
def upload_client_document(
    client_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return client_service.upload_document(
        db,
        client_id,
        file,
        str(current_user.id)
    )


@router.get(
    "/{client_id}/documents",
    response_model=list[ClientDocumentResponse]
)
def list_client_documents(
    client_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return client_service.list_documents(
        db,
        client_id,
        str(current_user.id)
    )

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.auth.dependencies import get_current_user

from app.modules.clients.presentation.schemas import (
    ClientCreate,
    ClientDocumentResponse,
    ClientResponse,
    ClientUpdate,
)

from app.modules.clients.application.use_cases import (
    CreateClientUseCase,
    GetClientUseCase,
    ListClientsUseCase,
    UpdateClientUseCase,
    UploadDocumentUseCase,
    ListDocumentsUseCase,
)

from app.modules.users.models import User


router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)


create_client_use_case = CreateClientUseCase()
list_clients_use_case = ListClientsUseCase()
get_client_use_case = GetClientUseCase()
update_client_use_case = UpdateClientUseCase()
upload_document_use_case = UploadDocumentUseCase()
list_documents_use_case = ListDocumentsUseCase()


@router.post(
    "",
    response_model=ClientResponse,
)
def create_client(
    data: ClientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_client_use_case.execute(
        db,
        data,
        str(current_user.id),
    )


@router.get(
    "",
    response_model=list[ClientResponse],
)
def list_clients(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return list_clients_use_case.execute(
        db,
        str(current_user.id),
    )


@router.get(
    "/{client_id}",
    response_model=ClientResponse,
)
def get_client(
    client_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_client_use_case.execute(
        db,
        client_id,
        str(current_user.id),
    )


@router.patch(
    "/{client_id}",
    response_model=ClientResponse,
)
def update_client(
    client_id: str,
    data: ClientUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_client_use_case.execute(
        db,
        client_id,
        data,
        str(current_user.id),
    )


@router.post(
    "/{client_id}/documents",
    response_model=ClientDocumentResponse,
)
def upload_client_document(
    client_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return upload_document_use_case.execute(
        db,
        client_id,
        file,
        str(current_user.id),
    )


@router.get(
    "/{client_id}/documents",
    response_model=list[ClientDocumentResponse],
)
def list_client_documents(
    client_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return list_documents_use_case.execute(
        db,
        client_id,
        str(current_user.id),
    )
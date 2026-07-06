from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):

    full_name: str
    dni: str | None = None
    birth_date: date | None = None
    accident_date: date | None = None
    address: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    notes: str | None = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):

    full_name: str | None = None
    dni: str | None = None
    birth_date: date | None = None
    accident_date: date | None = None
    address: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    notes: str | None = None


class ClientResponse(ClientBase):

    id: str
    data_source: str
    created_by_user_id: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class ClientDocumentResponse(BaseModel):

    id: str
    client_id: str
    original_filename: str
    stored_filename: str
    storage_path: str
    content_type: str | None
    size_bytes: int
    uploaded_by_user_id: str
    source: str
    ai_processing_status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

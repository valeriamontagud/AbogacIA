"""Tests HTTP del modulo de clientes."""


def _create_auth_header(client):
    email = "clients@example.com"
    password = "secret123"

    client.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Clients User",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )

    token = login_response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_create_list_and_update_client(client):
    auth_header = _create_auth_header(client)

    create_response = client.post(
        "/clients",
        headers=auth_header,
        json={
            "full_name": "Maria Lopez",
            "dni": "12345678A",
            "birth_date": "1985-03-12",
            "accident_date": "2026-01-20",
            "address": "Calle Mayor 1, Valencia",
            "phone": "600123123",
            "email": "maria@example.com",
            "notes": "Cliente creado manualmente.",
        },
    )

    assert create_response.status_code == 200
    created_client = create_response.json()
    assert created_client["full_name"] == "Maria Lopez"
    assert created_client["dni"] == "12345678A"
    assert created_client["data_source"] == "manual"

    list_response = client.get(
        "/clients",
        headers=auth_header,
    )

    assert list_response.status_code == 200
    clients = list_response.json()
    assert len(clients) == 1
    assert clients[0]["id"] == created_client["id"]

    update_response = client.patch(
        f"/clients/{created_client['id']}",
        headers=auth_header,
        json={
            "address": "Avenida Nueva 10, Valencia",
        },
    )

    assert update_response.status_code == 200
    assert update_response.json()["address"] == "Avenida Nueva 10, Valencia"


def test_list_client_documents_empty(client):
    auth_header = _create_auth_header(client)

    create_response = client.post(
        "/clients",
        headers=auth_header,
        json={
            "full_name": "Juan Perez",
        },
    )

    client_id = create_response.json()["id"]

    documents_response = client.get(
        f"/clients/{client_id}/documents",
        headers=auth_header,
    )

    assert documents_response.status_code == 200
    assert documents_response.json() == []

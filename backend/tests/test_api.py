"""Tests de integración HTTP para los endpoints principales.

Usan TestClient para validar rutas públicas y autenticadas.
"""


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_auth_register_login_and_me(client):
    # Registrar un usuario a través del endpoint /auth/register.
    email = "apiuser@example.com"
    password = "secret123"

    register_response = client.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "API User"
        }
    )

    assert register_response.status_code == 200
    register_data = register_response.json()
    assert register_data["email"] == email
    assert "id" in register_data

    login_response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    assert login_response.status_code == 200
    login_data = login_response.json()
    assert login_data["access_token"]
    assert login_data["token_type"] == "bearer"

    # Usar el token obtenido para llamar al endpoint protegido /auth/me.
    auth_header = {"Authorization": f"Bearer {login_data['access_token']}"}
    me_response = client.get("/auth/me", headers=auth_header)

    assert me_response.status_code == 200
    me_data = me_response.json()
    assert me_data["email"] == email
    assert me_data["full_name"] == "API User"

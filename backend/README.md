# AbogacIA

## Inicio rápido del entorno

Este proyecto usa Docker Compose para arrancar el backend, PostgreSQL y Redis.

### 1. Ir a la carpeta `backend`

```powershell
cd c:\Users\usuario\Desktop\AbogacIA\AbogacIA\backend
```

### 2. Levantar el entorno con Docker

```powershell
docker compose up --build
```

Esto crea y arranca tres servicios:
- `backend` con FastAPI en `http://localhost:8001`
- `postgres` en el puerto `5432`
- `redis` en el puerto `6379`

### 3. Entrar al contenedor del backend (opcional)

```powershell
docker compose exec backend bash
```

Dentro del contenedor el código ya está montado en `/app` y no necesitas buscar una carpeta `backend` adicional.

## Variables de entorno necesarias

El backend carga `backend/.env` con `pydantic-settings`.

Ejemplo de contenido para `backend/.env`:

```env
APP_NAME=AbogacIA
APP_ENV=development
API_V1_STR=/api/v1
SECRET_KEY=supersecretkey
POSTGRES_SERVER=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=abogacia
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/abogacia
REDIS_URL=redis://redis:6379
ACCESS_TOKEN_EXPIRE_MINUTES=10080
```

> Importante: no subas `backend/.env` a GitHub. Debe estar en `.gitignore`.

## Uso sin Docker (opcional)

Si prefieres instalar todo localmente:

```powershell
cd c:\Users\usuario\Desktop\AbogacIA\AbogacIA\backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

## Comprobación rápida

Abre en tu navegador:

```text
http://localhost:8001/
```

Deberías ver una respuesta JSON con el mensaje de la aplicación.

## Notas útiles

- El archivo principal es `backend/app/main.py`.
- El backend carga configuración desde `backend/app/config/settings.py`.
- Si `.env` ya estaba en Git, usa `git rm --cached backend/.env` para dejar de seguirlo.
- `backend/.env` y los entornos virtuales `venv/` no deben subirse a Git.
- El usuarios de prueba se llama test@example.com y contraseña 123456

## Como probar el usuario y contraseña 
- 1. Levantar backend, PostgreSQL y Redis

    cd backend
    docker compose up --build

    ## Dejar esa ventana abierta.
- 2. Ejecutar migraciones

    Abrir otro CMD:
    cd C:\Users\usuario\Desktop\AbogacIA\AbogacIA\backend
    docker compose exec backend alembic upgrade head

- 3. Comprobar que el backend funciona
    curl http://localhost:8001/health
    Debería devolver algo con:
    "status":"ok"

- 4. Crear usuario de prueba

    curl -X POST http://localhost:8001/auth/register -H "Content-Type: application/json" -d "{\"email\":\"test@example.com\",\"password\":\"123456\",\"full_name\":\"Usuario Test\"}"

- 5. Levantar frontend

    Abrir otro CMD:
    cd C:\Users\usuario\Desktop\AbogacIA\AbogacIA\frontend
    npm install
    npm run dev

- 6. Abrir la app
    Ir al navegador:
    http://localhost:3000/login
    Entrar con:
    Email: test@example.com
    Password: 123456

    ## Ahora mismo el login no redirige todavía; para comprobar que funciona hay que abrir la consola del navegador con F12 y ver que aparece el JWT recibido.

    ## Se ha creado un usuario que se llama lo siguiente para futuras pruebas

{
  "email": "admin@test.com",
  "password": "123456",
  "full_name": "Administrador"
}

## Se ha creado un cliente que se tiene estas caracteristicas 

{
  "full_name": "Juan Pérez",
  "dni": "12345678A",
  "birth_date": "1990-05-15",
  "accident_date": "2026-07-01",
  "address": "Calle Mayor 1",
  "phone": "600123123",
  "email": "juan@test.com",
  "notes": "Cliente de prueba"
}

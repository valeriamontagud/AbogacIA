# Pruebas del backend

Este directorio contiene tests para el backend de `AbogacIA`.

## ¿Qué se prueba?

1. `test_security.py`
   - Verifica que la función `hash_password` genera un hash distinto de la contraseña.
   - Verifica que `verify_password` aprueba la contraseña correcta y rechaza la incorrecta.
   - Verifica que `create_access_token` genera un JWT válido y que `decode_access_token` lo decodifica.
   - Verifica que un token inválido devuelve `None`.

2. `test_auth_service.py`
   - Verifica que `AuthService.register` crea un usuario nuevo correctamente.
   - Verifica que registrar un email duplicado lanza `BadRequestException`.
   - Verifica que `AuthService.login` devuelve un `access_token` válido.
   - Verifica que login con credenciales incorrectas lanza `UnauthorizedException`.

3. `test_repository.py`
   - Verifica que el repositorio de usuarios puede crear un usuario.
   - Verifica que el mismo repositorio puede recuperar ese usuario por email.

4. `test_api.py`
   - Verifica que el endpoint raíz `/` responde con código `200`.
   - Verifica el flujo completo de registro `/auth/register`, login `/auth/login` y acceso a `/auth/me`.

## Requisitos

Antes de ejecutar los tests, asegúrate de tener instaladas estas dependencias en el entorno virtual de `backend`:

- `pytest`
- `httpx`
- `fastapi`
- `sqlalchemy`
- `passlib`
- `python-jose`

Si no están instaladas, ejecuta desde `backend`:

```powershell
& "c:/Users/usuario/Desktop/AbogacIA/AbogacIA/venv/Scripts/python.exe" -m pip install pytest httpx
```

## Ejecutar pruebas

Desde la carpeta `backend` en PowerShell:

```powershell
Set-Location 'c:\Users\usuario\Desktop\AbogacIA\AbogacIA\backend'
& '..\venv\Scripts\python.exe' -m pytest tests -q
```

> Nota: hay una advertencia conocida de `pythonjsonlogger` que no afecta al resultado de los tests. Se ha añadido `backend/pytest.ini` para silenciarla.

## Qué debe salir

- Todos los tests deben pasar.
- No debe haber errores ni fallos.
- El resumen final debe mostrar algo como:

```text
=== 5 passed in X.XXs ===
```

Si un test falla, revisa el mensaje de error para identificar qué parte del flujo (seguridad, auth, repositorio o API) está fallando.

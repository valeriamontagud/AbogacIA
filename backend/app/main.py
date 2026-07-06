from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.shared.logger.logger import setup_logging
from app.shared.middleware.middleware import LoggingMiddleware
from app.modules.auth.router import router as auth_router
from app.modules.clients.router import router as clients_router

from app.shared.exceptions.exceptions import AppException

from app.modules.health.router import (
    router as health_router
)

from app.shared.exceptions.handlers import (
    app_exception_handler,
    generic_exception_handler
)

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# Exception handlers
# =========================================================

app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

#app.add_middleware(LoggingMiddleware)

app.include_router(auth_router)
app.include_router(clients_router)
app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} funcionando"
    }

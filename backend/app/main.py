from fastapi import FastAPI
from app.config.settings import settings
from app.shared.logger.logger import setup_logging
from app.shared.logger.middleware import LoggingMiddleware
from app.modules.auth.router import router as auth_router

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

#app.add_middleware(LoggingMiddleware)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} funcionando"
    }
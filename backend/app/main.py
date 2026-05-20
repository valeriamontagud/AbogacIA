from fastapi import FastAPI
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} funcionando"
    }
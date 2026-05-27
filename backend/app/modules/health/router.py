"""
Healthcheck router.
"""

from fastapi import APIRouter
from sqlalchemy import text

from app.database.session import SessionLocal


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
def healthcheck():
    """
    Healthcheck aplicación.
    """

    database_status = "ok"

    try:

        db = SessionLocal()

        db.execute(
            text("SELECT 1") #Comprobar postgreSQL
        )

    except Exception:

        database_status = "error"

    finally:

        db.close()

    return {
        "status": "ok",
        "services": {
            "api": "ok",
            "database": database_status,
        }
    }
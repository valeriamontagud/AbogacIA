"""
Handlers globales de exceptions.
"""

import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.shared.exceptions.exceptions import AppException


logger = logging.getLogger(__name__)


async def app_exception_handler(
    request: Request,
    exc: AppException
):
    """
    Handler exceptions controladas.
    """

    logger.warning(
        f"App exception: {exc.code} - {exc.message}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    """
    Handler exceptions inesperadas.
    """

    logger.exception("Unhandled exception")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "internal_server_error",
                "message": "Internal server error"
            }
        }
    )
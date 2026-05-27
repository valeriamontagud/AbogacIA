import time
import uuid
import logging

from starlette.middleware.base import BaseHTTPMiddleware

from app.shared.logger.request_context import (
    request_id_context
)

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        # =====================================================
        # Generar request id único
        # =====================================================

        request_id = str(uuid.uuid4())

        request_id_context.set(request_id)

        # =====================================================
        # Inicio request
        # =====================================================

        start_time = time.time()

        logger.info(
            f"Request started {request.method} {request.url.path}"
        )

        # =====================================================
        # Ejecutar request
        # =====================================================

        response = await call_next(request)

        # =====================================================
        # Tiempo ejecución
        # =====================================================

        duration = round(
            time.time() - start_time,
            4
        )

        # =====================================================
        # Log final
        # =====================================================

        logger.info(
            (
                f"Request completed "
                f"{request.method} "
                f"{request.url.path} "
                f"status={response.status_code} "
                f"duration={duration}s"
            )
        )

        # =====================================================
        # Header tracing
        # =====================================================

        response.headers["X-Request-ID"] = request_id

        return response
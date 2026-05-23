import time
import uuid
import logging
#Se utiliza para saber el request_id en el logger, para poder rastrear las peticiones en los logs.

from starlette.middleware.base import BaseHTTPMiddleware

from app.shared.logger.request_context import (
    request_id_context
)

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        request_id = str(uuid.uuid4())

        request_id_context.set(request_id)

        start_time = time.time()

        logger.info(
            "Request started",
            extra={
                "method": request.method,
                "path": request.url.path,
            }
        )

        response = await call_next(request)

        duration = time.time() - start_time

        logger.info(
            "Request completed",
            extra={
                "status_code": response.status_code,
                "duration": duration,
            }
        )

        response.headers["X-Request-ID"] = request_id

        return response
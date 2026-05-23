
#Se utiliza para saber el request_id en el logger, para poder rastrear las peticiones en los logs.

from contextvars import ContextVar


request_id_context: ContextVar[str] = ContextVar(
    "request_id",
    default=""
)
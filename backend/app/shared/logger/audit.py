"""
Audit logger.

Centraliza eventos auditables del sistema.
"""

import logging


# Logger especializado auditoría
logger = logging.getLogger("audit")


def audit_log(
    action: str,
    user_id: str | None = None,
    entity: str | None = None,
    entity_id: str | None = None
):
    """
    Registrar evento auditoría.
    """

    logger.info(
        (
            f"AUDIT "
            f"action={action} "
            f"user_id={user_id} "
            f"entity={entity} "
            f"entity_id={entity_id}"
        )
    )
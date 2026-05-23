import logging
import sys

from pythonjsonlogger import jsonlogger

from app.shared.logger.request_context import (
    request_id_context
)


class RequestIdFilter(logging.Filter):

    def filter(self, record):

        record.request_id = request_id_context.get()

        return True


def setup_logging():

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s %(request_id)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.addFilter(RequestIdFilter())
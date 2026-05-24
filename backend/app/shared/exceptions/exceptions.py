"""
Exceptions globales de la aplicación.
"""


class AppException(Exception):
    """
    Exception base de la app.
    """

    def __init__(
        self,
        message: str,
        code: str,
        status_code: int = 400
    ):
        self.message = message
        self.code = code
        self.status_code = status_code


class NotFoundException(AppException):

    def __init__(self, message="Resource not found"):
        super().__init__(
            message=message,
            code="not_found",
            status_code=404
        )


class UnauthorizedException(AppException):

    def __init__(self, message="Unauthorized"):
        super().__init__(
            message=message,
            code="unauthorized",
            status_code=401
        )


class BadRequestException(AppException):

    def __init__(self, message="Bad request"):
        super().__init__(
            message=message,
            code="bad_request",
            status_code=400
        )
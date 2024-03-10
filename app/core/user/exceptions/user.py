from app.core.shared.exception_base import BaseException


class AuthError(BaseException):
    """Raised when a user cannot pass the authentication"""

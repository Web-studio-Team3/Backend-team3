from core.shared.exceptions import BaseException


class AuthError(BaseException):
    """Raised when a user cannot pass the authentication"""
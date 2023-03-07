from passlib.context import CryptContext
from core.user.protocols.hasher_password import HasherPassword

from settings import Settings


class HasherPasswordImp(HasherPassword):
    settings = Settings
    _pwd_context = CryptContext(schemes=[settings.password_algorithm], deprecated="auto")

    def hash(self, password: str) -> str:
        return self._pwd_context.hash(password)

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(raw_password, hashed_password)

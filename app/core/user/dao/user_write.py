from typing import Protocol
from app.core.user.dto.user import UserSignUpHash


class UserWrite(Protocol):
    def create(self, user: UserSignUpHash) -> None:
        raise NotImplementedError

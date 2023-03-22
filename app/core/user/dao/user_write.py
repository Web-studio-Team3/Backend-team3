from typing import Protocol
from app.core.user.dto.user import (
    UserSignUpHash, UserId, UserUpdateWithId
)


class UserWrite(Protocol):
    def create(self, user: UserSignUpHash) -> None:
        raise NotImplementedError

    def delete(self, user_id: UserId) -> None:
        raise NotImplementedError

    def update(self, user: UserUpdateWithId) -> None:
        raise NotImplementedError

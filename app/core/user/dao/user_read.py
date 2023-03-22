from typing import Protocol
from app.core.user.entities.user import User
from app.core.user.dto.user import UserGetByEmailResp


class UserRead(Protocol):
    def get_by_email(self, email: str) -> UserGetByEmailResp:
        raise NotImplementedError

    def get_by_id(self, id: str) -> User:
        raise NotImplementedError

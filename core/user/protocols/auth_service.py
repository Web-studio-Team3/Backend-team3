from typing import Protocol
from core.user import dto
from uuid import UUID


class AuthService(Protocol):

    async def login(self, user: dto.UserLogin) -> UUID:
        raise NotImplementedError

    async def register(self, user: dto.UserRegister) -> None:
        raise NotImplementedError

    async def logout(self, user: dto.UserLogout) -> None:
        raise NotImplementedError

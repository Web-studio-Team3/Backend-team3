from typing import Protocol
from core.user import entities
from uuid import UUID


class UserWriteDao(Protocol):
    async def create(self, user: entities.User) -> None:
        raise NotImplementedError

    async def update(self, user: entities.User) -> None:
        raise NotImplementedError

    async def delete(self, user_id: UUID):
        raise NotImplementedError

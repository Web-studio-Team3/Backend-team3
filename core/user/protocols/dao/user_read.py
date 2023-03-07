from typing import Protocol
from core.user.entities.value_objects.email import Email
from core.user import entities
from uuid import UUID


class UserReadDao(Protocol):
    async def get_by_email(self, email: Email) -> entities.User:
        raise NotImplementedError

    async def get_by_id(self, user_id: UUID) -> entities.User:
        raise NotImplementedError

from typing import Protocol
from core.user import dto
from uuid import UUID


class UserSessionReadDao(Protocol):
    async def get(self, session_id: UUID) -> dto.SessionRead | None:
        raise NotImplementedError
   
from typing import Protocol
from core.user import dto


class UserSessionWriteDao(Protocol):

    async def create(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError

    async def update(self, session: dto.SessionWrite) -> None:
        raise NotImplementedError

    async def delete(self, session_id: str) -> None:
        raise NotImplementedError

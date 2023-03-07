from shared.dto import BaseDto
from uuid import UUID


class SessionRead(BaseDto):
    jwt_token: str | None


class SessionWrite(SessionRead):
    session_id: UUID
    jwt_token = str
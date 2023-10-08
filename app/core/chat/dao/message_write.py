from app.core.chat.dto.message import CreateMessage, MessagesId
from typing import Protocol


class MessageWrite(Protocol):
    def create(self, message: CreateMessage) -> None:
        raise NotImplementedError

    def delete(self, message_id: MessagesId) -> None:
        raise NotImplementedError

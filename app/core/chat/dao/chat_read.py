from typing import Protocol
from app.core.chat.entities.chat import Chat
from app.core.chat.entities.message import Message


class ChatRead(Protocol):
    def get_by_id(self, chat_id: str) -> Chat:
        raise NotImplementedError

    def get_all_messages_by_id(self, messages_id: str) -> list[Message]:
        raise NotImplementedError

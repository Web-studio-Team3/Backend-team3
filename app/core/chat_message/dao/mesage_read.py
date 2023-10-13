from typing import Protocol
from app.core.chat_message.enteties.message import Message


class MessageRead(Protocol):
    def get_all_messages_by_id(self, messages_id: str) -> list[Message]:
        raise NotImplementedError
from typing import Protocol

from app.core.chat_message.dto.message import MessagesId
from app.core.chat_message.enteties.message import Message

#Интиерфейс для чтения всех сообщений
class MessageRead(Protocol):
    def get_all_messages_by_id(self, messages_id: MessagesId) -> list[Message]:
        raise NotImplementedError

from typing import Protocol
from app.core.chat_message.dto.message import MessagesId
from app.core.chat_message.dto.message import ChatMessages


#Интиерфейс для чтения всех сообщений
class MessagesRead(Protocol):
    def get_all_messages_by_id(self, messages_id: MessagesId) -> ChatMessages:
        raise NotImplementedError

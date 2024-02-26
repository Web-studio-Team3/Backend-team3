from typing import Protocol
from app.core.chat_message.dto.message import Message, MessagesId


# Абстрактный клас для взаимодействия с сообщениями
class MessageWrite(Protocol):
    def create(self, messages_id: MessagesId) -> MessagesId:
        raise NotImplementedError

    def update(self, messages_id: MessagesId, message: Message) -> Message:
        raise NotImplementedError

    def add_message(self, messages_id: MessagesId, message: Message) -> None:
        raise NotImplementedError

    def delete_all_message(self, messages_id: MessagesId) -> None:
        raise NotImplementedError

    def delete_message(self, message_id: MessagesId) -> None:
        raise NotImplementedError

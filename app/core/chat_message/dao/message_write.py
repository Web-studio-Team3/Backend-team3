from app.core.chat_message.dto.message import Message, MessagesId
from typing import Protocol


class MessageWrite(Protocol):
    def create(self, messages_id: MessagesId) -> MessagesId:
        raise NotImplementedError

    def add_message(self, message: Message) -> None:
        raise NotImplementedError

    def delete_all_message(self, messages_id: MessagesId) -> None:
        raise NotImplementedError

    def delete_message(self, message_id: Message.message_id) -> None:
        raise NotImplementedError

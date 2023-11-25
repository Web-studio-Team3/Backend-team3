from typing import Protocol

from app.core.chat_message.dto.message import Message, MessageId


class MessageWrite(Protocol):
    def create(self, messages_id: MessageId) -> MessageId:
        raise NotImplementedError

    def add_message(self, message: Message) -> None:
        raise NotImplementedError

    def delete_all_message(self, messages_id: MessageId) -> None:
        raise NotImplementedError

    def delete_message(self, message_id: MessageId) -> None:
        raise NotImplementedError

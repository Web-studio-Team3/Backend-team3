from typing import Protocol
from app.core.chat_message.dto.message import MessagesId
from app.core.chat_message.dto.message import AllMessages


class MessagesRead(Protocol):
    def get_all_messages_by_id(self, messages_id: MessagesId) -> AllMessages:
        raise NotImplementedError

from app.core.chat.dto.chat import CreateChat, ChatId
from typing import Protocol


class ChatWrite(Protocol):
    def create(self, chat: CreateChat) -> None:
        raise NotImplementedError

    def delete(self, chat_id: ChatId) -> None:
        raise NotImplementedError
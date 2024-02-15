from typing import Protocol

from app.core.chat.dto.chat import ChatId, CreateChat


class ChatWrite(Protocol):
    def create(self, chat: CreateChat) -> ChatId:
        raise NotImplementedError

    def delete(self, chat_id: ChatId) -> None:
        raise NotImplementedError

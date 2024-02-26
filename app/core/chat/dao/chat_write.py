from typing import Protocol

from app.core.chat.dto.chat import ChatId, CreateChat, ChatUpdateWithId


class ChatWrite(Protocol):
    def create(self, chat: CreateChat) -> ChatId:
        raise NotImplementedError

    def update(self, chat: ChatUpdateWithId) -> None:
        raise NotImplementedError

    def delete(self, chat_id: ChatId) -> None:
        raise NotImplementedError

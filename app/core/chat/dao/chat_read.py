from typing import Protocol
from app.core.chat.entities.chat import Chat



class ChatRead(Protocol):
    def get_by_id(self, chat_id: str) -> Chat:
        raise NotImplementedError

from app.shared.dto_base import BaseDto
from typing import Optional


class ChatId(BaseDto):
    id: str


class CreateChat(BaseDto):
    seller_id: str
    buyer_id: str


class ChatUpdate(BaseDto):
    id: Optional[str]
    seller_id: Optional[str]
    buyer_id: Optional[str]


class ChatUpdateWithId(BaseDto):
    id: str
    chat_update: ChatUpdate

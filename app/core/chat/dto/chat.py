from app.shared.dto_base import BaseDto


class ChatId(BaseDto):
    id: str


class CreateChat(BaseDto):
    seller_id: str
    buyer_id: str
    messages_id: str

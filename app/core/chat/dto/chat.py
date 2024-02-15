from app.shared.dto_base import BaseDto
from typing import Optional


# ID чата
class ChatId(BaseDto):
    id: str

# Объект для создания чата
class CreateChat(BaseDto):
    seller_id: str
    buyer_id: str
    #messages_id: Optional[str]




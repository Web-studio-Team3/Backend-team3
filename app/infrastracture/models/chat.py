from pydantic import BaseModel


class ChatModel(BaseModel):
    seller_id: str
    buyer_id: str
    item_id: str
    messages_id: str
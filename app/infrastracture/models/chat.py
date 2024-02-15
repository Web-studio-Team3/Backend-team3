from pydantic import BaseModel
from bson.objectid import ObjectId
from app.core.chat.entities.chat import Chat


class ChatModel(BaseModel):
    seller_id: ObjectId
    buyer_id: ObjectId
    # messages_id: ObjectId

    class Config:
        arbitrary_types_allowed = True


def from_entity(chat: Chat):
    return ChatModel(
        seller_id=ObjectId(chat.seller_id),
        buyer_id=ObjectId(chat.buyer_id),
        # messages_id=ObjectId(chat.messages_id),
    )

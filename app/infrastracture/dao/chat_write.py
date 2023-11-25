from bson import ObjectId

from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId, CreateChat
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.chat import ChatModel


class ChatWriteDaoImpl(BaseDao, ChatWrite):
    def create(self, chat: CreateChat) -> ChatId:
        messages = self._database.create_collection("chat")
        chat_id = (
            self._database["chat"]
            .insert_one(
                ChatModel(
                    seller_id=ObjectId(chat.seller_id),
                    buyer_id=ObjectId(chat.buyer_id),
                    messages_id=ObjectId(f"chat_{chat.seller_id + chat.buyer_id}"),
                )
            )
            .inserted_id
        )
        messages.rename(f"chat_{chat.seller_id + chat.buyer_id}")
        return ChatId(id=str(chat_id))

    def delete(self, chat_id: ChatId) -> None:
        self._database["chat"].find_one_and_delete({"_id": ObjectId(chat_id.id)})

from bson import ObjectId

from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId, CreateChat, ChatUpdateWithId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.chat import ChatModel


class ChatWriteDaoImpl(BaseDao, ChatWrite):
    def create(self, chat: CreateChat) -> ChatId:
        print("Creating chat...")
        chat_id = (
            self._database["chats"]
            .insert_one(
                ChatModel(
                    seller_id=ObjectId(chat.seller_id),
                    buyer_id=ObjectId(chat.buyer_id),
                ).dict(exclude_none=True)
            ).inserted_id
        )
        print(chat_id)
        print("The chat has been created")
        return ChatId(id=str(chat_id))

    def delete(self, chat_id: ChatId) -> None:
        self._database["chats"].find_one_and_delete({"_id": ObjectId(chat_id.id)})

    def update(self, chat: ChatUpdateWithId) -> None:
        self._database["chats"].find_one_and_update(
            {"_id": ObjectId(chat.id)},
            {"$set": chat.item_update.dict(exclude_none=True)},
        )

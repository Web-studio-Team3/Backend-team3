from bson import ObjectId

from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId, CreateChat
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.chat import ChatModel


class ChatWriteDaoImpl(BaseDao, ChatWrite):
    def create(self, chat: CreateChat) -> ChatId:
        print("Creating chat...")
        print(chat)
        #messages_id = self._database["messages"].insert_one({}).inserted_id
        chat_id = (
            self._database["chats"]
            .insert_one(
                ChatModel(
                    seller_id=ObjectId(chat.seller_id),
                    buyer_id=ObjectId(chat.buyer_id),
                    # messages_id="0-",
                ).dict(exclude_none=True)
            ).inserted_id
        )
        print(chat_id)
        print("The chat has been created")
        return ChatId(id=str(chat_id))

    def delete(self, chat_id: ChatId) -> None:
        chat = self._database["сhats"].find_one({"_id": ObjectId(id)})
        #self._database['messages'].find_one_and_delete({"_id": ObjectId(chat["messages_id"])})
        #self._database["chat"].find_one_and_delete({"_id":ObjectId(chat["_id"])})

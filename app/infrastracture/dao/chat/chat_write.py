from bson import ObjectId

from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId, CreateChat, ChatUpdateWithId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.chat import ChatModel

from app.core.chat_message.dto.message import AllMessages


class ChatWriteDaoImpl(BaseDao, ChatWrite):
    async def create(self, chat: CreateChat) -> ChatId:
        print("Creating messages...")
        messages_id = (
            await self._database["chat_messages"].insert_one(
                AllMessages()
            ).inserted_id
        )
        print("The messages has been created")
        print(messages_id)

        chat.messages_id = messages_id
        chat_id = (
            await self._database["chats"]
            .insert_one(
                ChatModel(
                    seller_id=ObjectId(chat.seller_id),
                    buyer_id=ObjectId(chat.buyer_id),
                    messages_id=ObjectId(chat.messages_id)
                ).dict(exclude_none=True)
            ).inserted_id
        )
        return ChatId(id=str(chat_id))

    def delete(self, chat_id: ChatId) -> None:
        self._database["chats"].find_one_and_delete({"_id": ObjectId(chat_id.id)})

    def update(self, chat: ChatUpdateWithId) -> None:
        self._database["chats"].find_one_and_update(
            {"_id": ObjectId(chat.id)},
            {"$set": chat.item_update.dict(exclude_none=True)},
        )

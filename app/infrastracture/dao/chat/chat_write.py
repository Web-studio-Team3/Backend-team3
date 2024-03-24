from bson import ObjectId
import datetime

from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId, CreateChat, ChatUpdateWithId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.chat import ChatModel

from app.core.chat_message.dto.message import AllMessages
from app.core.chat_message.dto.message import Message


class ChatWriteDaoImpl(BaseDao, ChatWrite):
    def create(self, chat: CreateChat) -> str:
        messages_id = (
            self._database["chat_messages"].insert_one(
                AllMessages(
                    messages=[Message(
                        date_time=str(datetime.datetime.now()),
                        user_name="",
                        message="",
                    )],
                ).dict(exclude_none=True)
            ).inserted_id
        )

        chat_id = (
            self._database["chats"]
            .insert_one(
                ChatModel(
                    seller_id=ObjectId(chat.seller_id),
                    buyer_id=ObjectId(chat.buyer_id),
                    messages_id=ObjectId(messages_id)
                ).dict(exclude_none=True)
            ).inserted_id
        )

        return str(chat_id)

    def delete(self, chat_id: ChatId) -> None:
        print(chat_id)
        chat = self._database["chats"].find_one({"_id": ObjectId(chat_id)})
        self._database["chat_messages"].find_one_and_delete({"_id": ObjectId(chat["messages_id"])})
        self._database["chats"].find_one_and_delete({"_id": ObjectId(chat_id)})

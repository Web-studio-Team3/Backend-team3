from bson import ObjectId
from app.infrastracture.dao.base import BaseDao

from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import CreateChat, ChatId
from app.infrastracture.models.chat import ChatModel
from app.core.chat_message.dto.message import MessagesId


class ChatWriteDaoImpl(BaseDao, ChatWrite):
    def create(self, chat: CreateChat) -> ChatId:
        messages = self._database.create_collection()
        chat_id = self._database["chat"].insert_one(
            ChatModel(
                seller_id=ObjectId(chat.seller_id),
                buyer_id=ObjectId(chat.buyer_id),
                item_id=ObjectId(chat.item_id),
                messages_id=ObjectId(messages.MessagesId(id=messages.create_index("chat_messages", unique=True)))
            )
        ).inserted_id
        return ChatId(id=str(chat_id))

    def delete(self, chat_id: ChatId) -> None:
        self._database["chat"].find_one_and_delete({"_id": ObjectId(chat_id.id)})

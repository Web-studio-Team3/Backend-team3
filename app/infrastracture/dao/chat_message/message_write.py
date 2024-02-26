from typing import Optional

from bson import ObjectId
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import Message, MessagesId, ChatMessages, MessageUpdateWithId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.message import MessageModel


class MessageWriteDaoImpl(BaseDao, MessageWrite):
    def create_messages(self, chat_messages: ChatMessages) -> None:
        message_id = self._database["messages"].insert_one(
            ChatMessages(
                chat_id=chat_messages.chat_id,
                messages=Optional[chat_messages.messages]
            ).inserted_id
        )

    def add_message(self, message: MessageUpdateWithId, messages_id: str) -> None:
        messages = (
            self._database["messages"].find_one_and_update(
                {"_id": ObjectId(message.id)},
                {"$set": message.message_update.dict(exclude_none=True)},
            )
        )

    def delete_all_message(self, messages_id: MessagesId, message: Message) -> None:
        self._database["messages"].find_one_and_delete(
            {"_id": ObjectId(message.id)}
        )

    def delete_message(self, messages_id: MessagesId, id: int) -> None:
        messages = self._database["messages"].find_one({"_id": ObjectId(messages_id.id)})
        messages.messages[id].pop()

from typing import Optional

from bson import ObjectId
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import Message, MessagesId, AllMessages, MessageUpdateWithId
from app.infrastracture.dao.base import BaseDao


class MessageWriteDaoImpl(BaseDao, MessageWrite):
    def add_message(self, message: MessageUpdateWithId, messages_id: str) -> None:
        messages = (
            self._database["messages"].find_one_and_update(
                {"_id": ObjectId(message.id)},
                {"$set": message.message_update.dict(exclude_none=True)},
            )
        )

    def delete_all_message(self, messages_id: MessagesId, message: Message) -> None:
        self._database["chat_messages"].find_one_and_delete(
            {"_id": ObjectId(message.id)}
        )

    # def delete_message(self, messages_id: MessagesId, id: int) -> None:
    #     messages = self._database["chat_messages"].find_one({"_id": ObjectId(messages_id)})
    #     messages.messages[id].pop()

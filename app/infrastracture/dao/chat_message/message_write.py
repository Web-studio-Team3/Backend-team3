from typing import Optional

from bson import ObjectId
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import Message, MessagesId, AllMessages, MessageUpdateWithId
from app.infrastracture.dao.base import BaseDao


class MessageWriteDaoImpl(BaseDao, MessageWrite):
    def add_message(self, messages_id: MessagesId, message: Message) -> None:
        self._database["chat_messages"].update_one(
            {"_id": ObjectId(messages_id)},
            {"$push": {"messages": message.dict(exclude_none=True)}},
        )

    def delete_all_messages(self, messages_id: MessagesId) -> None:
        messages = self._database["chat_messages"].find_one(
            {"_id": ObjectId(messages_id)})

        messages["messages"] = []

        self._database["chat_messages"].replace_one(
            {"_id": ObjectId(messages_id)}, messages)

    def delete_message(self, messages_id: MessagesId, message_id: str) -> None:
        messages = self._database["chat_messages"].find_one(
            {"_id": ObjectId(messages_id)})

        messages["messages"].pop(int(message_id))

        self._database["chat_messages"].replace_one(
            {"_id": ObjectId(messages_id)}, messages)

from app.infrastracture.dao.base import BaseDao
from bson import ObjectId
from app.infrastracture.models.message import MessageModel
from app.core.chat_message.dto.message import MessageId, Message
from app.core.chat_message.dao.message_write import MessageWrite


class MessageWriteDaoImpl(BaseDao, MessageWrite):
    def add_message(self, message: Message, messages_id: str) -> None:
        messages = self._database[f"{messages_id}"].insert_one(
            MessageModel(
                message_id=message.message_id,
                user_name=message.user_name,
                date_time=message.date_time,
                message=message.message
            )
        ).inserted_id

    def delete_all(self, messages_id: MessageId) -> None:
        self._database[f"{messages_id}"].drop()

    def delete(self, messages_id: MessageId, message: Message) -> None:
        self._database[f"{messages_id}"].find_one_and_delete({"_id": ObjectId(message.id)})

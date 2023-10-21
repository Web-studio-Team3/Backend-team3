from app.infrastracture.dao.base import BaseDao
from bson import ObjectId
from app.infrastracture.models.message import MessageModel
from app.core.chat_message.dto.message import MessagesId, Message


class MessageWriteDaoImpl(BaseDao, Message):
    def add_message(self, messages_id: MessagesId, message: Message) -> None:
        message_id = self._database[f"{messages_id}"].insert_one(
            MessageModel(
                message_id=message.message_id,
                user_name=message.user_name,
                datetime=message.datetime,
                message=message.message
            )
        )

    def delete_all(self, messages_id: MessagesId):
        self._database[f"{messages_id}"].drop()

    def delete(self,messages_id: MessagesId,message: Message.message_id):
        self._database[f"{messages_id}"].find_one_and_delete({"_id": ObjectId(message.id)})

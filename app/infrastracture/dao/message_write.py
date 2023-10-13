from app.infrastracture.dao.base import BaseDao
from bson import ObjectId

from app.core.chat_message.dao.message_write import  MessageWrite
from app.infrastracture.models.message import MessageModel
from app.core.chat_message.dto.message import MessagesId,CreateMessage


class NessageEriteDaoImpl(BaseDao, CreateMessage):
    def create(self,message: CreateMessage) -> MessagesId:
        message_id = self._database["message"].insert_one(
            MessageModel(
                user_name = message.user_name,
                datetime = message.datetime,
                message = message.message
            )
        )
    def delete(self, message: MessagesId):
        self._database["message"].find_one_and_delete({"_id": ObjectId(message.id)})


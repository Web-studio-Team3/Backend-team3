from bson import ObjectId
from app.core.chat_message.dao.message_read import MessagesRead
from app.core.chat_message.enteties.message import Message, AllMessages
from app.infrastracture.dao.base import BaseDao


class MessageReadDaoImpl(BaseDao, MessagesRead):
    def get_all_messages_by_id(self, messages_id: str) -> AllMessages:
        messages_obj = self._database["chat_messages"].find_one({"_id": ObjectId(messages_id)})
        if not messages_obj:
            raise TypeError
        messages = [i for i in messages_obj["messages"]]
        return messages

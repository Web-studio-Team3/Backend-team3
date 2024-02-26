from bson import ObjectId
from app.core.chat_message.dao.message_read import MessagesRead
from app.core.chat_message.enteties.message import Message, ChatMessages
from app.infrastracture.dao.base import BaseDao


class MessageReadDaoImpl(BaseDao, MessagesRead):
    def get_all_messages_by_id(self, messages_id: str) -> ChatMessages:
        messages = self._database["messages"].find_one({"_id": ObjectId(messages_id)})
        if not messages:
            raise TypeError
        return messages

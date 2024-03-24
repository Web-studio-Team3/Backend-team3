from bson import ObjectId

from app.core.chat.dao.chat_read import ChatRead
from app.core.chat.entities.chat import Chat
from app.infrastracture.dao.base import BaseDao


class ChatReadDaoImpl(BaseDao, ChatRead):
    def get_by_id(self, chat_id: str) -> Chat:
        chat = self._database["chats"].find_one({"_id": ObjectId(chat_id)})
        if not chat:
            raise TypeError

        return Chat(
            id=str(chat["_id"]),
            seller_id=str(chat["seller_id"]),
            buyer_id=str(chat["buyer_id"]),
            messages_id=str(chat["messages_id"]),
        )

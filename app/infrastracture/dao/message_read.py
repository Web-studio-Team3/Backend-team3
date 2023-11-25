from app.core.chat_message.dao.message_read import MessageRead
from app.core.chat_message.enteties.message import Message
from app.infrastracture.dao.base import BaseDao


class MessageReadDaoImpl(BaseDao, MessageRead):
    def get_all_messages_by_id(self, messages_id: str) -> list[Message]:
        messages = self._database[f"{messages_id}"].find()
        if not messages:
            raise TypeError
        messages_res = []
        for item in messages:
            messages_res.append(
                Message(
                    id=str(messages["_id"]),
                    user_name=messages["user_name"],
                    data_time=messages["data_time"],
                    mewssage=messages["message"],
                )
            )
        return messages_res

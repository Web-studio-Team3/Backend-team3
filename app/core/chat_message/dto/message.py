from typing import Optional, List
from app.shared.dto_base import BaseDto


# ID сообщений
class MessagesId(BaseDto):
    id: str


# Объект сообщения
class Message(BaseDto):
    id: int
    date_time: str
    user_name: str
    message: str


# Объект сообщений для 1 чата
class ChatMessages(BaseDto):
    chat_id: str
    messages: Optional[List[Message]]


class UpdateMessage(BaseDto):
    chat_id: Optional[str]
    date_time: Optional[str]
    message: Optional[str]


class MessageUpdateWithId(BaseDto):
    id: str
    message_update: UpdateMessage

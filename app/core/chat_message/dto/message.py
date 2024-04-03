from typing import Optional
from app.shared.dto_base import BaseDto


# ID сообщений
class MessagesId(BaseDto):
    id: str


# Объект сообщения
class Message(BaseDto):
    date_time: str
    user_name: str
    message: str


# Объект сообщений для 1 чата
class AllMessages(BaseDto):
    messages: Optional[list[Message]]


class UpdateMessage(BaseDto):
    date_time: Optional[str]
    message: Optional[str]


class MessageUpdateWithId(BaseDto):
    id: int
    message_update: UpdateMessage

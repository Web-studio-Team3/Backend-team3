import datetime as datetime
from app.shared.dto_base import BaseDto


class MessagesId(BaseDto):
    id: str


class Messages(BaseDto):
    message_id: str


class Message(BaseDto):
    user_name: str
    datetime: datetime
    message: str

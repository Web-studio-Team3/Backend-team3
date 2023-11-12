from app.shared.dto_base import BaseDto


class MessageId(BaseDto):
    id: str


class Message(BaseDto):
    user_name: str
    date_time: str
    message: str

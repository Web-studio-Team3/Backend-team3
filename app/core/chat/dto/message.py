import datetime as datetime
from typing import Optional
from app.shared.dto_base import BaseDto


class MessagesId(BaseDto):
    id: str


class CreateMessage(BaseDto):
    message_id: str
    user_name: str
    datetime: datetime
    message: str

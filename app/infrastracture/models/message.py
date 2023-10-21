from pydantic import BaseModel
import datetime


class MessageModel(BaseModel):
    message_id: str
    user_name: str
    datetime: datetime
    message: str
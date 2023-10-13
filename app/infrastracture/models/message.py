from pydantic import BaseModel
import datetime


class MessageModel(BaseModel):
    user_name: str
    datetime: datetime
    message: str
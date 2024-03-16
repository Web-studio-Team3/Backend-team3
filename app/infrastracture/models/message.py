from pydantic import BaseModel


class MessageModel(BaseModel):
    date_time: str
    message: str

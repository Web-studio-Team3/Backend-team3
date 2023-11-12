from pydantic import BaseModel


class MessageModel(BaseModel):
    message_id: str
    user_name: str
    date_time: str
    message: str
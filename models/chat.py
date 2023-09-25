from pydantic import BaseModel, Field
from typing import Optional

#class ChatList(BaseModel):

class Chat(BaseModel):
    #_id
    chat_id: Optional[int] = Field(...)
    message: Optional[str] = Field(...)

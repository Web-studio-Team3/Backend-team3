from typing import Optional

from pydantic import BaseModel, Field


class Chat(BaseModel):
    # chat_id: str
    client_id: Optional[str] = Field(...)  # usr_id
    seller_id: Optional[str] = Field(...)  # usr_id
    message: Optional[str] = Field(...)

from dataclasses import dataclass
from typing import List
from app.core.chat_message.dto.message import Message


@dataclass
class ChatMessages:
    chat_id: str
    messages: List[Message]

@dataclass
class Message:
    user_name: str
    date_time: str
    message: str

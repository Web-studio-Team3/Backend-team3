from dataclasses import dataclass


@dataclass
class Message:
    chat_id: str
    user_name: str
    date_time: str
    message: str

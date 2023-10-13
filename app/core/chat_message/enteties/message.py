from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    message_id: str
    user_name: str
    datetime: datetime
    message: str

from dataclasses import dataclass


@dataclass
class Message:
    user_name: str
    date_time: str
    message: str


@dataclass
class AllMessages:
    id: str
    messages: list[Message]




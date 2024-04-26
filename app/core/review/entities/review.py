from dataclasses import dataclass


@dataclass
class Review:
    id: str
    user_id: str
    item_id: str
    text: str
    full_name: str
    rating: str

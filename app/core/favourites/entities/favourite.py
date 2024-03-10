from dataclasses import dataclass


@dataclass
class Favourite:
    id: str
    user_id: str
    item_id: str

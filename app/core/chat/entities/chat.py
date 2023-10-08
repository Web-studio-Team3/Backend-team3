from dataclasses import dataclass
from datetime import date


@dataclass
class Chat:
    id: str
    seller_id: str
    buyer_id: str
    item_id: str
    messages_id: str

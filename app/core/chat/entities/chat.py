from dataclasses import dataclass


@dataclass
class Chat:
    id: str
    seller_id: str
    buyer_id: str
    messages_id: str

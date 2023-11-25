from dataclasses import dataclass


@dataclass
class SoldItemRelation:
    id: str
    seller_id: str
    buyer_id: str
    item_id: str

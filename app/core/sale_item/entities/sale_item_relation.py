from dataclasses import dataclass


@dataclass
class SaleItemRelation:
    id: str
    user_id: str
    item_id: str

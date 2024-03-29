from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    id: str
    category_id: str
    title: str
    description: str
    condition: str
    address: str
    cost: str
    status: str
    buyer_id: Optional[str]
    seller_id: str

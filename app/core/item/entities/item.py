from dataclasses import dataclass


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
    
from dataclasses import dataclass


@dataclass
class PictureItemRelation:
    id: str
    picture_id: str
    item_id: str

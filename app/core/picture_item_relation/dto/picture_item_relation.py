from app.shared.dto_base import BaseDto


class PictureItemRelation(BaseDto):
    picture_id: str
    item_id: str


class PictureItemRelationId(BaseDto):
    id: str


class PictureItemRelationItemId(BaseDto):
    item_id:str

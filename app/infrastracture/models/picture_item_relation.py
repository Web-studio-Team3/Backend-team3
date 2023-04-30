from pydantic import BaseModel


class PictureItemRelationModel(BaseModel):
    picture_id: str
    item_id: str

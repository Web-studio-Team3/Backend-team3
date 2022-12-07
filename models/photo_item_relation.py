from pydantic import BaseModel, Field


class PhotoItemRelation(BaseModel):
    photo_url: str = Field(...)
    item_id: str = Field(...)

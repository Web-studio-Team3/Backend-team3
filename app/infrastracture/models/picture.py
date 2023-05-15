from pydantic import BaseModel


class PictureModel(BaseModel):
    picture_ulr: str

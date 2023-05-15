from pydantic import BaseModel


class FavouriteModel(BaseModel):
    user_id: str
    item_id: str

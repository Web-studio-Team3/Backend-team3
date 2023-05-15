from pydantic import BaseModel


class SoldItemRelationModel(BaseModel):
    seller_id: str
    buyer_id: str
    item_id: str

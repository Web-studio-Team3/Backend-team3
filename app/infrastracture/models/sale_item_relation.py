from pydantic import BaseModel


class SaleItemRelationModel(BaseModel):
    user_id: str
    item_id: str

from pydantic import BaseModel


class ReviewModel(BaseModel):
    user_id: str
    item_id: str
    text: str
    full_name: str


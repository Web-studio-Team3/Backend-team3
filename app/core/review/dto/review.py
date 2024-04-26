from app.shared.dto_base import BaseDto


class Review(BaseDto):
    user_id: str
    item_id: str
    text: str
    full_name: str


class ReviewId(BaseDto):
    id: str


class ReviewItemId(BaseDto):
    item_id: str


class ReviewUserId(BaseDto):
    user_id: str


class CreateReviewRequest(BaseDto):
    item_id: str
    text: str
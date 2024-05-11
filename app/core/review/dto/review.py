from app.shared.dto_base import BaseDto

from typing import Optional


class Review(BaseDto):
    id: Optional[str]
    user_id: str
    item_id: str
    text: str
    full_name: str
    rating: str


class ReviewId(BaseDto):
    id: str


class ReviewItemId(BaseDto):
    item_id: str


class ReviewUserId(BaseDto):
    user_id: str


class CreateReviewRequest(BaseDto):
    item_id: str
    text: str
    rating: str


class ReviewUpdate(BaseDto):
    user_id: Optional[str]
    item_id: Optional[str]
    text: Optional[str]
    full_name: Optional[str]
    rating: Optional[str]


class ReviewUpdateWithId(BaseDto):
    id: str
    review_update: ReviewUpdate
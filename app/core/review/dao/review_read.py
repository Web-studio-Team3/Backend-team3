from typing import Protocol

from app.core.review.entities.review import Review


class ReviewRead(Protocol):
    def get_reviews_by_item_id(self, item_id: str) -> list[Review]:
        raise NotImplementedError
    
    def get_reviews_by_user_id(self, user_id: str) -> list[Review]:
        raise NotImplementedError
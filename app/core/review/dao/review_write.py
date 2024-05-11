from typing import Protocol

from app.core.review.dto.review import Review, ReviewId, ReviewUpdateWithId


class ReviewWrite(Protocol):
    def create(self, review: Review) -> ReviewId:
        raise NotImplementedError

    def delete(self, review_id: str) -> None:
        raise NotImplementedError
    
    def update(self, item: ReviewUpdateWithId) -> Review:
        raise NotImplementedError

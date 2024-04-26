from typing import Protocol

from app.core.review.dto.review import Review, ReviewId


class ReviewWrite(Protocol):
    def create(self, review: Review) -> ReviewId:
        raise NotImplementedError

    def delete(self, review_id: str) -> None:
        raise NotImplementedError

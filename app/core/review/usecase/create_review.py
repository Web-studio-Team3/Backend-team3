from app.core.review.dao.review_write import ReviewWrite
from app.core.review.dto.review import Review, ReviewId
from app.core.shared.usecase_base import UseCase


class CreateReviewUseCase(UseCase[Review, ReviewId]):
    def __init__(self, write_dao: ReviewWrite):
        self._write_dao = write_dao

    def execute(self, obj: Review) -> ReviewId:
        return self._write_dao.create(review=obj)

from app.core.review.dao.review_read import ReviewRead
from app.core.review.dao.review_write import ReviewWrite
from app.core.review.dto.review import ReviewUpdateWithId
from app.core.review.entities.review import Review
from app.core.shared.usecase_base import UseCase


class UpdateReviewUseCase(UseCase[ReviewUpdateWithId, Review]):
    def __init__(self, review_write_dao: ReviewWrite):
        self._review_write_dao = review_write_dao

    def execute(self, updated_review: ReviewUpdateWithId) -> Review:
        return self._review_write_dao.update(updated_review)

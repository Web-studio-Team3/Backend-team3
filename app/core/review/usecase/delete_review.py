from app.core.review.dao.review_write import ReviewWrite
from app.core.review.dto.review import ReviewId
from app.core.shared.usecase_base import UseCase


class DeleteReviewUseCase(UseCase[ReviewId, None]):
    def __init__(self, review_write_dao: ReviewWrite):
        self._review_write_dao = review_write_dao

    def execute(self, review_id: ReviewId) -> None:
        self._review_write_dao.delete(review_id=review_id.id)

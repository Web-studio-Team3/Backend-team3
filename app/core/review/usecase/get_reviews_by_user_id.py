from app.core.review.dao.review_read import ReviewRead
from app.core.review.dto.review import Review, ReviewUserId
from app.core.shared.usecase_base import UseCase


class GetReviewsByUserIdUseCase(UseCase[ReviewUserId, list[Review]]):
    def __init__(self, read_dao=ReviewRead):
        self._read_dao = read_dao

    def execute(self, obj: ReviewUserId) -> list[Review]:
        return self._read_dao.get_reviews_by_user_id(user_id=obj.user_id)

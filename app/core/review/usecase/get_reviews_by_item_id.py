from app.core.review.dao.review_read import ReviewRead
from app.core.review.dto.review import ReviewItemId, Review
from app.core.shared.usecase_base import UseCase


class GetReviewsByItemIdUseCase(UseCase[ReviewItemId, list[Review]]):
    def __init__(self, read_dao=ReviewRead):
        self._read_dao = read_dao

    def execute(self, obj: ReviewItemId) -> list[Review]:
        return self._read_dao.get_reviews_by_item_id(item_id=obj.item_id)

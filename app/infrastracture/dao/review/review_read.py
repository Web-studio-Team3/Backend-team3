from bson import ObjectId

from app.core.review.dao.review_read import ReviewRead
from app.core.review.entities.review import Review
from app.infrastracture.dao.base import BaseDao


class ReviewReadImpl(BaseDao, ReviewRead):
    def get_reviews_by_item_id(self, item_id: str) -> list[Review]:
        reviews = self._database["review"].find({"item_id": item_id})
        if not reviews:
            raise TypeError
        
        return list(map(create_review, reviews))
    
    def get_reviews_by_user_id(self, user_id: str) -> list[Review]:
        reviews = self._database["review"].find({"user_id": user_id})
        if not reviews:
            raise TypeError

        return list(map(create_review, reviews))


def create_review(review_db_object):
    return Review(
        id=str(review_db_object["_id"]),
        user_id=review_db_object["user_id"],
        item_id=review_db_object["item_id"],
        text=review_db_object["text"],
        full_name=review_db_object["full_name"]
    )

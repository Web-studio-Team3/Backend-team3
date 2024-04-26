from bson import ObjectId

from app.core.review.dao.review_write import ReviewWrite
from app.core.review.dto.review import Review, ReviewId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.review import ReviewModel


class ReviewWriteImpl(BaseDao, ReviewWrite):
    def create(self, review: Review) -> ReviewId:
        inserted_id = (
            self._database["review"]
            .insert_one(
                ReviewModel(
                    user_id=review.user_id, 
                    item_id=review.item_id, 
                    text=review.text, 
                    full_name=review.full_name,
                    rating=review.rating
                ).dict(exclude_none=True)
            )
            .inserted_id
        )
        return ReviewId(id=str(inserted_id))

    def delete(self, review_id: str) -> None:
        self._database["review"].delete_one({"_id": ObjectId(review_id)})

from bson import ObjectId

from app.core.review.dao.review_write import ReviewWrite
from app.core.review.dto.review import Review, ReviewId, ReviewUpdateWithId
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
    
    def update(self, review: ReviewUpdateWithId) -> Review:
        self._database["review"].find_one_and_update(
            {"_id": ObjectId(review.id)},
            {"$set": review.review_update.dict(exclude_none=True)},
        )
        review = self._database["review"].find_one({"_id": ObjectId(review.id)})
        if not review:
            raise TypeError

        return Review(
            id=str(review["_id"]),
            user_id=str(review["user_id"]),
            item_id=str(review["item_id"]),
            text=review["text"],
            full_name=review["full_name"],
            rating=review["rating"]
        )
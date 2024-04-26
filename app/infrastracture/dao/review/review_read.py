from bson import ObjectId

from app.core.review.dao.review_read import ReviewRead
from app.core.review.entities.review import Review
from app.infrastracture.dao.base import BaseDao


# class ReviewReadImpl(BaseDao, ReviewRead):
#     def get_reviews_by_item_id(self, item_id: str) -> list[Review]:
#         reviews = self._database["review"].find({"item_id": item_id})
#         if not reviews:
#             raise TypeError
        
#         user_ids = {review["user_id"] for review in reviews}
        
#         users = self._database["users"].find({"_id": {"$in": list(map(ObjectId, user_ids))}})
#         user_dict = {str(user["_id"]): user["full_name"] for user in users}

#         return [create_review(review, user_dict.get(review["user_id"], "Unknown")) for review in reviews]

class ReviewReadImpl(BaseDao, ReviewRead):
    def get_reviews_by_item_id(self, item_id: str) -> list[Review]:
        reviews = self._database["review"].find({"item_id": item_id})
        if not reviews:
            raise TypeError
        
        return list(map(create_review, reviews))

# def create_review(review_db_object, full_name):
#     return Review(
#         id=str(review_db_object["_id"]),
#         user_id=review_db_object["user_id"],
#         item_id=review_db_object["item_id"],
#         text=review_db_object["text"],
#         full_name=full_name,
#     )

def create_review(review_db_object):
    return Review(
        id=str(review_db_object["_id"]),
        user_id=review_db_object["user_id"],
        item_id=review_db_object["item_id"],
        text=review_db_object["text"],
        full_name=review_db_object["full_name"]
    )

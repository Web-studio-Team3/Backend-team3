from app.infrastracture.dao.base import BaseDao
from app.core.user.dao.user_read import UserRead
from uuid import UUID
from app.core.user.dto.user import UserGetByEmailResp
from app.core.user.entities.user import User
from bson import ObjectId


class UserReadDaoImpl(
    BaseDao, UserRead
):
    def get_by_email(self, email: str) -> UserGetByEmailResp:
        user = self._database["user"].find_one({"email": email})
        return UserGetByEmailResp(
            user_id=str(user["_id"]),
            hashed_password=str(user["hashed_password"])
        )

    def get_by_id(self, id: str) -> User:
        user = self._database["user"].find_one({"_id": id})
        if not user:
            raise TypeError
        return User(
            id=user["_id"],
            email=user["email"],
            hashed_password=user["hashed_password"],
            full_name=user["full_name"],
            date_of_birth=user["date_of_birth"]
        )

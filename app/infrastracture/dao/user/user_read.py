from bson import ObjectId

from app.core.user.dao.user_read import UserRead
from app.core.user.dto.user import UserGetByEmailResp
from app.core.user.entities.user import User
from app.infrastracture.dao.base import BaseDao


class UserReadDaoImpl(BaseDao, UserRead):
    def get_by_email(self, email: str) -> UserGetByEmailResp:
        user = self._database["user"].find_one({"email": email})
        if not user:
            raise TypeError
        return UserGetByEmailResp(
            user_id=str(user["_id"]), hashed_password=str(user["hashed_password"])
        )

    def get_by_id(self, id: str) -> User:
        user = self._database["user"].find_one({"_id": ObjectId(id)})
        if not user:
            raise TypeError
        if "telegram_id" in user.keys():
            return User(
                id=str(user["_id"]),
                email=user["email"],
                hashed_password=user["hashed_password"],
                full_name=user["full_name"],
                date_of_birth=user["date_of_birth"],
                picture_id=user["picture_id"],
                telegram_id=user["telegram_id"],
                telegram_username=user["telegram_username"],
            )
        else:
            return User(
                id=str(user["_id"]),
                email=user["email"],
                hashed_password=user["hashed_password"],
                full_name=user["full_name"],
                date_of_birth=user["date_of_birth"],
                picture_id=user["picture_id"],
                telegram_id=None,
                telegram_username=None,
            )


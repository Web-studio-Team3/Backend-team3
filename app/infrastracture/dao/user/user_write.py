from typing import Optional

from bson import ObjectId

from app.core.user.dao.user_write import UserWrite
from app.core.user.dto.user import UserId, UserSignUpHash, UserUpdateWithId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.user import UserModel


class UserWriteDaoImpl(BaseDao, UserWrite):
    def create(self, user: UserSignUpHash) -> None:
        saved_user = self._database["user"].find_one({"email": user.email})

        if not saved_user:
            self._database["user"].insert_one(
                UserModel(
                    email=user.email,
                    hashed_password=user.hashed_password,
                    full_name=user.full_name,
                    date_of_birth=user.date_of_birth,
                    picture_id=user.picture_id,
                    telegram_id=user.telegram_id,
                    telegram_username=user.telegram_username,
                ).dict(exclude_none=True)
            )
        else:
            raise IndexError

    def delete(self, user_id: UserId) -> None:
        self._database["user"].find_one_and_delete({"_id": ObjectId(user_id.id)})

    def update(self, user: UserUpdateWithId) -> None:
        self._database["user"].find_one_and_update(
            {"_id": ObjectId(user.id)},
            {"$set": user.user_update.dict(exclude_none=True)},
        )

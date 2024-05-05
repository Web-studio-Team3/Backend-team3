from bson import ObjectId

from app.core.token.dao.token_write import RefreshTokenWrite
from app.core.token.dto.token import (
    RefreshTokenDto,
    AccessTokenUpdateDto,
    AccessTokenUserIdDto,
)
from app.core.token.entities.token import RefreshToken
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.token import RefreshTokenModel


class RefreshTokenWriteDaoImpl(BaseDao, RefreshTokenWrite):
    def create(self, token: RefreshTokenDto) -> RefreshToken:
        access_token = self._database["tg-token"].insert_one(
            RefreshTokenModel(user_id=token.user_id, jwt_token=token.token).dict(
                exclude_none=True
            )
        )

        return RefreshToken(
            id=access_token.inserted_id, user_id=token.user_id, jwt_token=token.token
        )

    def update(self, token: AccessTokenUpdateDto) -> RefreshToken:
        self._database["tg-token"].find_one_and_update(
            {"_id": ObjectId(token.id)},
            {"$set": {"user_id": token.user_id, "jwt_token": token.token}},
        )

        updated_token = self._database["token"].find_one({"_id": ObjectId(token.id)})
        return RefreshToken(
            id=str(updated_token["_id"]),
            user_id=updated_token["user_id"],
            jwt_token=updated_token["jwt_token"],
        )

    def delete_by_user_id(self, token: AccessTokenUserIdDto) -> None:
        self._database["token"].find_one_and_delete({"user_id": token.user_id})

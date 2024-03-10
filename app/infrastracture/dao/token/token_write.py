from bson import ObjectId

from app.core.token.dao.token_write import TokenWrite
from app.core.token.dto.token import (
    AccessTokenDto,
    AccessTokenUpdateDto,
    AccessTokenUserIdDto,
)
from app.core.token.entities.token import AccessToken
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.token import AccessTokenModel


class TokenWriteDaoImpl(BaseDao, TokenWrite):
    def create(self, token: AccessTokenDto) -> AccessToken:
        access_token = self._database["token"].insert_one(
            AccessTokenModel(user_id=token.user_id, jwt_token=token.token).dict(
                exclude_none=True
            )
        )
        return AccessToken(
            id=access_token.inserted_id, user_id=token.user_id, jwt_token=token.token
        )

    def update(self, token: AccessTokenUpdateDto) -> AccessToken:
        self._database["token"].find_one_and_update(
            {"_id": ObjectId(token.id)},
            {"$set": {"user_id": token.user_id, "jwt_token": token.token}},
        )

        updated_token = self._database["token"].find_one({"_id": ObjectId(token.id)})
        return AccessToken(
            id=str(updated_token["_id"]),
            user_id=updated_token["user_id"],
            jwt_token=updated_token["jwt_token"],
        )

    def delete_by_user_id(self, token: AccessTokenUserIdDto) -> None:
        self._database["token"].find_one_and_delete({"user_id": token.user_id})

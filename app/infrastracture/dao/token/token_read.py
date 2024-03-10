from app.core.token.dao.token_read import TokenRead
from app.core.token.entities.token import AccessToken
from app.infrastracture.dao.base import BaseDao


class TokenReadDaoImpl(BaseDao, TokenRead):
    def get_by_user_id(self, user_id: str) -> AccessToken:
        access_token = self._database["token"].find_one({"user_id": user_id})
        if not access_token:
            raise TypeError
        return AccessToken(
            id=access_token["_id"],
            user_id=access_token["user_id"],
            jwt_token=access_token["jwt_token"],
        )

    def get_by_token(self, token: str) -> AccessToken:
        access_token = self._database["token"].find_one({"jwt_token": token})
        return AccessToken(
            id=access_token["_id"],
            user_id=access_token["user_id"],
            jwt_token=access_token["jwt_token"],
        )

from app.core.token.dao.token_read import TokenRead
from app.core.token.entities.token import RefreshToken
from app.infrastracture.dao.base import BaseDao


class TokenReadDaoImpl(BaseDao, TokenRead):
    def get_by_user_id(self, user_id: str) -> RefreshToken:
        access_token = self._database["tg-token"].find_one({"user_id": user_id})
        if not access_token:
            raise TypeError
        return RefreshToken(
            id=access_token["_id"],
            user_id=access_token["user_id"],
            jwt_token=access_token["jwt_token"],
        )

    def get_by_token(self, token: str) -> RefreshToken:
        access_token = self._database["token"].find_one({"jwt_token": token})
        return RefreshToken(
            id=access_token["_id"],
            user_id=access_token["user_id"],
            jwt_token=access_token["jwt_token"],
        )

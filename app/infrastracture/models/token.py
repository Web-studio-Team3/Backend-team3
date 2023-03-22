from pydantic import BaseModel
from app.core.user.entities.token import AccessToken
from uuid import UUID


class AccessTokenModel(BaseModel):
    user_id: str
    jwt_token: str


def from_entity(access_token: AccessToken) -> AccessTokenModel:
    return AccessTokenModel(
        user_id=access_token.user_id,
        jwt_token=access_token.jwt_token
    )

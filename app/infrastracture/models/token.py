from pydantic import BaseModel
from app.core.token.entities.token import AccessToken


class AccessTokenModel(BaseModel):
    user_id: str
    jwt_token: str


def from_entity(access_token: AccessToken) -> AccessTokenModel:
    return AccessTokenModel(
        user_id=access_token.user_id,
        jwt_token=access_token.jwt_token
    )

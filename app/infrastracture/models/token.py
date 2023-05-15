from pydantic import BaseModel


class AccessTokenModel(BaseModel):
    user_id: str
    jwt_token: str

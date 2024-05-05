from dataclasses import dataclass


@dataclass
class AccessToken:
    id: str
    user_id: str
    jwt_token: str


@dataclass
class RefreshToken:
    id: str
    user_id: str
    jwt_token: str

from dataclasses import dataclass
from uuid import UUID


@dataclass
class AccessToken:
    id: str
    user_id: str
    jwt_token: str

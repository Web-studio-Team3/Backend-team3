from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    password_algorithm: str = Field(..., env='PASSWORD_ALGORITHM')

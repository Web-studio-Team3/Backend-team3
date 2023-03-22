from typing import Protocol
from pymongo.database import Database


class Dao(Protocol):
    def __init__(self, database: Database) -> None:
        raise NotImplementedError


class BaseDao(Dao):
    def __init__(self, database: Database) -> None:
        self._database = database

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from app.shared.dto_base import BaseDto

DtoType = TypeVar('DtoType', bound=BaseDto)
ReturnType = TypeVar('ReturnType')


class UseCase(ABC, Generic[DtoType, ReturnType]):
    def __init__(self):
        ...

    @abstractmethod
    def execute(self, obj: DtoType) -> ReturnType:
        raise NotImplementedError
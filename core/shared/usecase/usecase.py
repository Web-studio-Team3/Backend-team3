from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from shared import dto

DtoType = TypeVar('DtoType', bound=dto.BaseDto)
ReturnType = TypeVar('ReturnType')


class UseCase(ABC, Generic[DtoType, ReturnType]):
    def __init__(self):
        ...

    @abstractmethod
    async def execute(self, obj: DtoType) -> ReturnType:
        raise NotImplementedError

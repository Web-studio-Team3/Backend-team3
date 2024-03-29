from abc import ABC, abstractmethod
from typing import Generic, TypeVar

RequestType = TypeVar("RequestType")
ReturnType = TypeVar("ReturnType")


class PictureUseCase(ABC, Generic[RequestType, ReturnType]):
    def __init__(self):
        ...

    @abstractmethod
    def execute(self, request_var: RequestType) -> ReturnType:
        raise NotImplementedError

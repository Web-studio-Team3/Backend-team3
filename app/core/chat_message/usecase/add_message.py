from app.core.chat_message.dto.message import Message
from app.core.chat_message.enteties.message import Message
from app.core.shared.usecase_base import UseCase


class AddMessageUseCase(UseCase):
    def __init__(self, dao: Message):
        self._dao = dao

    def execute(self, message: Message) -> None:
        try:
            message = Message(
                user_name=message.user_name,
                datetime=message.datetime,
                message=message.message
            )
        except TypeError:
            raise TypeError

        try:
            return self._dao.create(message=message)
        except TypeError:
            raise TypeError

from app.core.chat_message.dto.message import CreateMessage
from app.core.shared.usecase_base import UseCase


class AddMessageUseCase(UseCase):
    def __init__(self, dao: CreateMessage):
        self._dao = dao

    def execute(self, message: CreateMessage) -> None:
        try:
            message = Message(
                message_id=message.message_id,
                user_name=message.user_name,
                datetime=message.datetime,
                message=message.message
            )
        except TypeError:
            raise TypeError

        try:
            print("create item use case")
            return self._dao.create(message=message)
        except TypeError:
            raise TypeError

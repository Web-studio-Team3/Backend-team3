from app.core.chat_message.dto.message import Message
from app.core.chat_message.enteties.message import Message
from app.core.shared.usecase_base import UseCase


class AddMessageUseCase(UseCase):
    def __init__(self, write_dao: Message):
        self.write_dao = write_dao

    def execute(self, message: Message) -> None:
        try:
            message = Message(
                chat_id=message.chat_id,
                user_name=message.user_name,
                date_time=message.date_time,
                message=message.message,
            )
        except TypeError:
            raise TypeError

        try:
            return self.write_dao.create(message=message)
        except TypeError:
            raise TypeError

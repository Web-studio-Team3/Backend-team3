from app.core.shared.usecase_base import UseCase

from app.core.chat_message.dto.message import Message
from app.core.chat_message.dto.message import MessageId
from app.core.chat_message.dao.message_write import MessageWrite


class DeleteMessageUseCase(UseCase[Message, None]):
    def __init__(
            self,
            message_write_dao: MessageWrite
    ):
        self._message_write_dao = message_write_dao

    def execute(self, message_id: MessageId) -> None:
        self._chat_write_dao.delete(messge_id=message_id)
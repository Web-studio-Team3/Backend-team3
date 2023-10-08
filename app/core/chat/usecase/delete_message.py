from app.core.shared.usecase_base import UseCase

from app.core.chat.dto.message import CreateMessage
from app.core.chat.dao.message_write import MessageWrite


class DeleteChatUseCase(UseCase[CreateMessage, None]):
    def __init__(
            self,
            message_write_dao: MessageWrite
    ):
        self._message_write_dao = message_write_dao

    def execute(self, message_id: CreateMessage.message_id) -> None:
        self._chat_write_dao.delete(messge_id=message_id)

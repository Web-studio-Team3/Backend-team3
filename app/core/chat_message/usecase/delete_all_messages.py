from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import MessagesId
from app.core.shared.usecase_base import UseCase


class DeleteAllMessagesUseCase(UseCase[MessagesId, None]):
    def __init__(
            self,
            message_write_dao: MessageWrite
    ):
        self._message_write_dao = message_write_dao

    def execute(self, messages_id: MessagesId) -> None:
        self._chat_write_dao.delete(messages_id=messages_id)
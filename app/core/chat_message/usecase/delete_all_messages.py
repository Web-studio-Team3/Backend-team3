from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import MessageId
from app.core.shared.usecase_base import UseCase


class DeleteAllMessagesUseCase(UseCase[MessageId, None]):
    def __init__(self, write_dao: MessageWrite):
        self.write_dao = write_dao

    def execute(self, messages_id: MessageId) -> None:
        self.write_dao.delete(messages_id=messages_id)

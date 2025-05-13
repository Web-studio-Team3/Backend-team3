from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import Message, MessagesId
from app.core.shared.usecase_base import UseCase


class DeleteMessageUseCase(UseCase[Message, None]):
    def __init__(self, write_dao: MessageWrite):
        self.write_dao = write_dao

    def execute(self, messages_id: str, message_id: str) -> None:
        self.write_dao.delete_message(messages_id=messages_id, message_id=message_id)

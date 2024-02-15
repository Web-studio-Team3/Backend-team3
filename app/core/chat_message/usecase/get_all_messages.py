from app.core.chat_message.dao.message_read import MessageRead
from app.core.chat_message.dto.message import MessagesId
from app.core.chat_message.enteties.message import Message
from app.core.shared.usecase_base import UseCase


class GetAllMessagesUseCase(UseCase[MessagesId, list[Message]]):
    def __init__(self, read_dao: MessageRead):
        self.read_dao = read_dao

    def execute(self, messages_id: str) -> list[Message]:
        try:
            messages = self.read_dao.get_all_messages_by_id(messages_id)
        except TypeError:
            raise TypeError
        return messages

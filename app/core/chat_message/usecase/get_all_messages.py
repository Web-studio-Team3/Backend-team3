from app.core.chat_message.dto.message import MessageId
from app.core.chat_message.dao.message_read import MessageRead
from app.core.chat_message.enteties.message import Message
from app.core.shared.usecase_base import UseCase


class GetAllMessagesUseCase(UseCase[MessageId, list[Message]]):

    def __init__(self, dao: MessageRead):
        self._dao = dao

    def execute(self, message_id: MessageId) -> list[Message]:
        try:
            messages = self._dao.get_all_messages_by_id(message_id)
        except TypeError:
            raise TypeError
        return messages

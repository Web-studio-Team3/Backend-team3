from app.core.chat_message.dao.message_read import MessagesRead
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import MessageUpdateWithId
from app.core.chat_message.enteties.message import Message,ChatMessages
from app.core.shared.usecase_base import UseCase


class AddMessageUseCase(UseCase[MessageUpdateWithId, Message]):
    def __init__(self, chat_message_write_dao: MessageWrite, chat_message_read_dao: MessagesRead):
        self._chat_message_write_dao = chat_message_write_dao
        self._chat_message_read_dao = chat_message_read_dao

    def execute(self, updated_message: MessageUpdateWithId, chat_messages: ChatMessages) -> Message:
        self._chat_message_write_dao.update(updated_message)
        return self._chat_message_read_dao.get_by_id(updated_message.id)

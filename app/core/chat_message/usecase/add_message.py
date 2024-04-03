from app.core.chat_message.dao.message_read import MessagesRead
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import MessageUpdateWithId
from app.core.chat_message.enteties.message import Message, AllMessages
from app.core.shared.usecase_base import UseCase


class AddMessageUseCase(UseCase[MessageUpdateWithId, Message]):
    def __init__(self, chat_message_write_dao: MessageWrite, chat_message_read_dao: MessagesRead):
        self._chat_message_write_dao = chat_message_write_dao
        self._chat_message_read_dao = chat_message_read_dao

    def execute(self, message: Message) -> None:
        self._chat_message_write_dao.add_message(message)

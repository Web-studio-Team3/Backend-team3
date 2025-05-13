from app.core.chat_message.dao.message_read import MessagesRead
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import MessageUpdateWithId
from app.core.chat_message.enteties.message import Message, AllMessages
from app.core.shared.usecase_base import UseCase


class AddMessageUseCase(UseCase[MessageUpdateWithId, Message]):
    def __init__(self, write_dao: MessageWrite):
        self.write_dao = write_dao
        #self.read_dao = read_dao

    def execute(self, messages_id: str, message: Message) -> None:
        self.write_dao.add_message(messages_id, message)

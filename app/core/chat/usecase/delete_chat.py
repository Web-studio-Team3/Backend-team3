from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId
from app.core.chat_message.dao.message_write import MessageWrite
from app.core.chat_message.dto.message import MessageId
from app.core.shared.usecase_base import UseCase


class DeleteChatUseCase(UseCase[MessageId, None]):
    def __init__(self, write_dao: ChatWrite, message_write_dao: MessageWrite):
        self.write_dao = write_dao
        self._message_write_dao = message_write_dao

    def execute(self, chat_id: ChatId, message_id: MessageId) -> None:
        self._message_write_dao.delete_all_message(message_id=message_id)
        self._chat_write_dao.delete(chat_id=chat_id)

from app.core.shared.usecase_base import UseCase

from app.core.chat.dto.message import MessagesId
from app.core.chat.dao.message_write import MessageWrite
from app.core.chat.dto.chat import ChatId
from app.core.chat.dao.chat_write import ChatWrite


class DeleteChatUseCase(UseCase[MessagesId, None]):
    def __init__(
            self,
            chat_write_dao: ChatWrite,
            message_write_dao: MessageWrite
    ):
        self._chat_write_dao = chat_write_dao
        self._message_write_dao = message_write_dao

    def execute(self, chat_id: ChatId, message_id: MessagesId) -> None:
        self._chat_write_dao.delete(messge_id=message_id)
        self._chat_write_dao.delete(chat_id=chat_id)

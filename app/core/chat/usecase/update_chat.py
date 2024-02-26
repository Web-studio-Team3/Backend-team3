from app.core.chat.dao.chat_read import ChatRead
from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatUpdateWithId
from app.core.chat.entities.chat import Chat
from app.core.shared.usecase_base import UseCase


class UpdateChatUseCase(UseCase[ChatUpdateWithId, Chat]):
    def __init__(self, chat_write_dao: ChatWrite, chat_read_dao: ChatRead):
        self._chat_write_dao = chat_write_dao
        self._chat_read_dao = chat_read_dao

    def execute(self, updated_chat: ChatUpdateWithId) -> Chat:
        self._chat_write_dao.update(updated_chat)
        return self._chat_read_dao.get_by_id(updated_chat.id)
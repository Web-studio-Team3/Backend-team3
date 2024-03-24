from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId
from app.core.shared.usecase_base import UseCase


class DeleteChatUseCase(UseCase[ChatId, None]):
    def __init__(self, write_dao: ChatWrite):
        self.write_dao = write_dao

    def execute(self, chat_id: ChatId) -> None:
        self.write_dao.delete(chat_id=chat_id)

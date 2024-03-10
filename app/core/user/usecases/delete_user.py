from app.core.shared.usecase_base import UseCase
from app.core.token.dto.token import AccessTokenUserIdDto
from app.core.token.usecases.delete_token_by_user_id import DeleteTokenByUserIdUseCase
from app.core.user.dao.user_write import UserWrite
from app.core.user.dto.user import UserId


class DeleteUserUseCase(UseCase[UserId, None]):
    def __init__(
        self,
        user_write_dao: UserWrite,
        delete_token_by_user_id_use_case: DeleteTokenByUserIdUseCase,
    ):
        self._user_write_dao = user_write_dao
        self._delete_token_by_user_id_use_case = delete_token_by_user_id_use_case

    def execute(self, user_id: UserId) -> None:
        self._user_write_dao.delete(user_id=user_id)
        self._delete_token_by_user_id_use_case.execute(
            AccessTokenUserIdDto(user_id=user_id.id)
        )

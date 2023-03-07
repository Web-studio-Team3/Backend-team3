import uuid

from core.user.protocols.auth_service import AuthService
from core.user.protocols.jwt_service import JwtService
from core.user.protocols.hasher_password import HasherPassword

from core.user.protocols.dao.user_session_write import UserSessionWriteDao
from core.user.protocols.dao.user_session_read import UserSessionReadDao
from core.user.protocols.dao.user_write import UserWriteDao
from core.user.protocols.dao.user_read import UserReadDao
from core.shared.protocols import Committer

from core.user import dto
from core.user.entities import value_objects
from core.user import entities

from core.user.exceptions import AuthError


class AuthServiceImp(AuthService):
    def __init__(
            self,
            hasher_password: HasherPassword,
            jwt_service: JwtService,
            dao_user_session_write: UserSessionWriteDao,
            dao_user_session_read: UserSessionReadDao,
            dao_user_write: UserWriteDao,
            dao_user_read: UserReadDao,
            committer: Committer
    ):
        self._hasher_password = hasher_password
        self._jwt_service = jwt_service
        self._dao_user_session_write = dao_user_session_write
        self._dao_user_session_read = dao_user_session_read
        self._dao_user_write = dao_user_write
        self._dao_user_read = dao_user_read
        self._committer = committer

    async def register(self, user: dto.UserRegister) -> None:
        email = user.email
        raw_password = user.raw_password
        full_name = user.full_name
        date_of_birth = user.date_of_birth
        photo_id = user.photo_id

        try:
            raw_password = value_objects.RawPassword(raw_password)
            hashed_password = self._hasher_password.hash(raw_password.value)

            user = entities.User(
                email=value_objects.Email(email),
                hashed_password=value_objects.HashedPassword(hashed_password),
                fullname=full_name,
                date_of_birth=date_of_birth,
                photo_id=photo_id
            )
        except ValueError as e:
            raise AuthError(e)
        except TypeError as e:
            raise AuthError(e)

        try:
            await self._dao_user_write.create(user)
            await self._committer.commit()
        except IndexError:
            await self._committer.rollback()
            raise AuthError("user already exist")

    async def login(self, user: dto.UserLogin) -> int:
        user_entity = await self._dao_user_read.get_by_email(user.email)

        if not user_entity:
            raise AuthError("user not found")
        if not self._hasher_password.verify_password(
                user.password, user_entity.hashed_password
        ):
            raise AuthError("invalid password")

        session_id = uuid.uuid4()
        jwt_token = self._jwt_service.encode({"user_id": str(user_entity.id)})

        session_dto = dto.SessionWrite(
            session_id=session_id, jwt_token=jwt_token
        )

        await self._dao_user_session_write.create(session_dto)

        return session_id

    async def logout(self, user: dto.UserLogout) -> None:
        session_id = user.session_id
        try:
            await self._dao_user_session_read.get(session_id)
        except ValueError as e:
            raise AuthError(e)
        await self._dao_user_session_write.delete(session_id)

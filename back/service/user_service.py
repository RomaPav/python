from dto.user_request import UserRequest
from mapper.mapper import Mapper
from model.user import User
from repository.user_repository import UserRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    @staticmethod
    def validate_user(user: UserRequest) -> bool:
        if not user.login or not user.password:
            return False
        if len(user.password) < 8:
            return False
        if not user.email.__contains__("@"):
            return False
        return True

    def check_user_if_exist(self, user: UserRequest) -> bool:
        existing_user = self._user_repository.get_by_login(user.login)
        if existing_user:
            return True
        return False

    def get_user(self, user_request: UserRequest) -> None | User:
        if not self.validate_user(user_request):
            print("None")
            return None
        user: User = Mapper.request_to_entity(user_request)
        # return self._user_repository.get_user_by_login_and_password(user)
        print("Find")
        return self._user_repository.get_by_login(user.login)

    def update_user(self, user_request: UserRequest) -> bool:
        if not self.validate_user(user_request):
            return False
        if not self.check_user_if_exist(user_request):
            return False
        user: User = self.user_request_to_entity(user_request)
        user.password = pwd_context.hash(user_request.password)
        return self._user_repository.update_user(user)

    def delete_user(self, user_request: UserRequest) -> bool:
        if not self.validate_user(user_request):
            return False
        if not self.check_user_if_exist(user_request):
            return False
        user: User = Mapper.request_to_entity(user_request)
        return self._user_repository.delete_user(user)

    def user_request_to_entity(self, user: UserRequest):
        return User(id=user.id, login=user.login, password=user.password, is_active=False, email=user.email,
                    full_name=user.full_name, role=user.role)

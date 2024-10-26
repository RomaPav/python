from dto.user_request import UserRequest
from dto.user_response import UserResponse
from model.user import User


class Mapper:
    # @staticmethod
    # def entity_to_response(user: User):
    #     return UserResponse(login=user.login, password=user.password, token="", full_name=user.full_name,
    #                         email=user.email, role=user.role)
    #
    @staticmethod
    def request_to_entity(user: UserRequest):
        return User(login=user.login, password=user.password, is_active=False, email=user.email,
                    full_name=user.full_name, role=user.role)

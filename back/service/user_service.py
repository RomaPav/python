from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from dto.user_request import UserRequest
from mapper.mapper import Mapper
from model.user import User
from repository.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "my_very_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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

    def registry(self, user_request: UserRequest) -> bool:
        if not self.validate_user(user_request):
            return False
        if self.check_user_if_exist(user_request):
            print("exist")
            return False
        user: User = Mapper.request_to_entity(user_request)
        user.password = pwd_context.hash(user_request.password)
        print("create")
        return self._user_repository.add_user(user)

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
        user: User = Mapper.request_to_entity(user_request)
        return self._user_repository.update_user(user)

    def delete_user(self, user_request: UserRequest) -> bool:
        if not self.validate_user(user_request):
            return False
        if not self.check_user_if_exist(user_request):
            return False
        user: User = Mapper.request_to_entity(user_request)
        return self._user_repository.delete_user(user)

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        to_encode['role'] = data.get("role").dict()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("login")
            if username is None:
                raise HTTPException(status_code=403, detail="Token is invalid or expired")
            return payload
        except JWTError:
            raise HTTPException(status_code=403, detail="Token is invalid or expired")

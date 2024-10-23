from datetime import timedelta
from http import HTTPStatus

from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from dto.user_request import UserRequest
from enums.role import UserRole
from repository.user_repository import UserRepository
from service.user_service import UserService, ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context

user_service = UserService(UserRepository())
router = APIRouter()


@router.post("/register")
def register_user(user_request: UserRequest):
    status_create = user_service.registry(user_request)
    if not status_create:
        raise HTTPException(status_code=400, detail="Username already registered")
    return HTTPStatus.CREATED


@router.post("/login")
def login(user_request: UserRequest):
    status_create = user_service.get_user(user_request)
    if status_create is None:
        raise HTTPException(status_code=400, detail="Username already registered")
    return HTTPStatus.ACCEPTED


@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_service.get_user(
        UserRequest(login=form_data.username, password=form_data.password, full_name="", email="@",
                    role=UserRole.USER))
    if user is None or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = UserService.create_access_token(
        data={"login": user.login,
              "full_name": user.full_name,
              "email": user.email,
              "role": user.role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/verify-token/{token}")
async def verify_user_token(token: str):
    UserService.verify_token(token=token)
    return {"message": "Token is valid"}


@router.get("/")
async def get():
    return {"message": "Token is valid"}

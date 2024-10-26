from http import HTTPStatus

from fastapi import HTTPException, APIRouter

from dto.user_request import UserRequest
from repository.user_repository import UserRepository
from service.user_service import UserService

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

@router.get("/verify-token/{token}")
async def verify_user_token(token: str):
    UserService.verify_token(token=token)
    return {"message": "Token is valid"}

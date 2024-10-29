from http import HTTPStatus

from fastapi import HTTPException, APIRouter

from dto.user_request import UserRequest, UserUpdate
from repository.user_repository import UserRepository
from service.user_service import UserService

user_service = UserService(UserRepository())
router = APIRouter()




@router.put("/")
def update_coin(user_request: UserUpdate):
    data = user_service.update_user(user_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

# @router.get("/{id}")
# def get_by_id(id: int):
#     data = user_service.get(id)
#     # if not data:
#     #     raise HTTPException(status_code=400, detail="Something went wrong")
#     return {
#         "data": data,
#         "status": HTTPStatus.OK
#     }

# @router.delete("/{user_id}")
# def delete_coin(user_id: int):
#     data = user_service.delete_user(user_id)
#     if not data:
#         raise HTTPException(status_code=400, detail="Something went wrong")
#     return {
#         "data": data,
#         "status": HTTPStatus.NO_CONTENT
#     }

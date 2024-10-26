from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from dto.order.order_request import OrderBase, OrderCreate
from model.order import Order
from repository.order_repository import OrderRepository
from service.order_service import OrderService

order_service = OrderService(OrderRepository())
router = APIRouter()



@router.get("/")
def get():
    data = order_service.get()
    if data is None:
        raise HTTPException(status_code=400, detail="No data in base")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.post("/")
def add_order(order_request: OrderCreate):
    data = order_service.add_order(order_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.CREATED
    }

@router.put("/")
def update_order(order_request: OrderBase):
    data = order_service.update_order(order_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

@router.get("/{id}")
def get_by_id(id: int):
    data = order_service.get_by_id(id)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

@router.delete("/{order_id}")
def delete_order(order_id: int):
    data = order_service.delete_order(order_id)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.NO_CONTENT
    }


@router.get("/user-id/{user_id}")
async def get_by_user_id(user_id: int):
    data = order_service.get_by_user_id(user_id)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

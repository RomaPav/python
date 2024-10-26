from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from dto.bit.bit_request import BitUpdate, BitCreate
from repository.bit_repository import BitRepository
from service.bit_service import BitService

bit_service = BitService(BitRepository())
router = APIRouter()


# @router.get("/")
# def get():
#     data = coin_service.get()
#     if data is None:
#         raise HTTPException(status_code=400, detail="No data in base")
#     return {
#         "data": data,
#         "status": HTTPStatus.OK
#     }


@router.post("/")
def add_bit(bit_request: BitCreate):
    data = bit_service.add_bit(bit_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.CREATED
    }


@router.put("/")
def update_bit(bit_request: BitUpdate):
    data = bit_service.update_bit(bit_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.get("/{id}")
def get_by_id(id: int):
    data = bit_service.get_by_id(id)
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.get("/trade-lot/{id}")
def get_by_id(id: int):
    data = bit_service.get_by_trade_lot_id(id)
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

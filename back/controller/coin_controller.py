from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from dto.coin.coin_request import CoinCreate, CoinBase, CoinUpdate
from repository.coin_repository import CoinRepository
from service.coin_service import CoinService

coin_service = CoinService(CoinRepository())
router = APIRouter()



@router.get("/")
def get():
    data = coin_service.get()
    if data is None:
        raise HTTPException(status_code=400, detail="No data in base")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.post("/")
def add_coin(coin_request: CoinCreate):
    data = coin_service.add_coin(coin_request)
    # if not data:
    #     raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.CREATED
    }

@router.put("/")
def update_coin(coin_request: CoinUpdate):
    data = coin_service.update_coin(coin_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

@router.get("/{id}")
def get_by_id(id: int):
    data = coin_service.get_by_id(id)
    # if not data:
    #     raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }

@router.delete("/{coin_id}")
def delete_coin(coin_id: int):
    data = coin_service.delete_coin(coin_id)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.NO_CONTENT
    }


from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from dto.trade_lot.trade_lot_request import TradeLotCreate, TradeLotBase, TradeLotUpdate
from model.trade_lot import TradeLot
from repository.trade_lot_repository import TradeLotRepository
from service.trade_lot_service import TradeLotService

trade_lot_service = TradeLotService(TradeLotRepository())
router = APIRouter()


@router.get("/")
def get():
    data = trade_lot_service.get()
    if data is None:
        raise HTTPException(status_code=400, detail="No data in base")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.post("/")
def add_trade_lot(trade_lot_request: TradeLotCreate):
    data = trade_lot_service.add_trade_lot(trade_lot_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.CREATED
    }


@router.put("/")
def update_trade_lot(trade_lot_request: TradeLotUpdate):
    data = trade_lot_service.update_trade_lot(trade_lot_request)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.delete("/{trade_lot_id}")
def delete_trade_lot(trade_lot_id: int):
    data = trade_lot_service.delete_trade_lot(trade_lot_id)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.NO_CONTENT
    }


@router.get("/coin-id/{coin_id}")
async def get_by_coin_id(coin_id: int):
    data = trade_lot_service.get_by_coin_id(coin_id)
    if not data:
        raise HTTPException(status_code=400, detail="Something went wrong")
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.get("/id/{id}")
def get_by_id(id: int):
    data = trade_lot_service.get_by_id(id)
    return {
        "data": data,
        "status": HTTPStatus.OK
    }


@router.get("/started/")
def active_trade_lot():
    data = trade_lot_service.active_trade_lot()
    return {
        "data": data,
        "status": HTTPStatus.OK
    }
#
@router.get("/started-for-buying/")
def active_trade_lot_for_buying():
    data = trade_lot_service.active_trade_lot_for_buying()
    return {
        "data": data,
        "status": HTTPStatus.OK
    }
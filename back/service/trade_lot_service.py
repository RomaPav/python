from dto.coin.coin_request import CoinBase
from dto.trade_lot.trade_lot_request import TradeLotBase, TradeLotCreate, TradeLotResponse
from model.trade_lot import TradeLot
from repository.trade_lot_repository import TradeLotRepository


class TradeLotService:
    def __init__(self, trade_lot_repository: TradeLotRepository):
        self._trade_lot_repository = trade_lot_repository

    @staticmethod
    def validate_trade_lot(trade_lot: TradeLot) -> bool:
        if not trade_lot.coin_id or not trade_lot.trade_status:
            return False
        return True

    def get(self):
        response = []
        for trade_lot in self._trade_lot_repository.get():
            response.append(self.trade_lot_to_trade_lot_response(trade_lot))
        return response

    def add_trade_lot(self, trade_lot: TradeLotCreate):
        db_trade_lot = TradeLot(**trade_lot.dict())
        if not self.validate_trade_lot(db_trade_lot):
            return None
        return self._trade_lot_repository.add_trade_lot(db_trade_lot)

    def update_trade_lot(self, trade_lot: TradeLotBase) -> bool:
        db_trade_lot = TradeLot(**trade_lot.dict())
        if not self.validate_trade_lot(db_trade_lot):
            return False
        return self._trade_lot_repository.update_trade_lot(db_trade_lot)

    def delete_trade_lot(self, id: int) -> bool:
        return self._trade_lot_repository.delete_trade_lot(id)

    def get_by_coin_id(self, coin_id: int):
        response = []
        for trade_lot in self._trade_lot_repository.get_by_coin_id(coin_id):
            response.append(self.trade_lot_to_trade_lot_response(trade_lot))
        return self._trade_lot_repository.get_by_coin_id(coin_id)

    def get_by_id(self, id: int):
        return self.trade_lot_to_trade_lot_response(self._trade_lot_repository.get_by_id(id))


    def active_trade_lot(self):
        response = []
        for trade_lot in self._trade_lot_repository.active_trade_lot():
            response.append(self.trade_lot_to_trade_lot_response(trade_lot))
        return response

    def active_trade_lot_for_buying(self):
        response = []
        for trade_lot in self._trade_lot_repository.active_trade_lot_for_buying():
            response.append(self.trade_lot_to_trade_lot_response(trade_lot))
        return response

    def trade_lot_to_trade_lot_response(self, trade_lot: TradeLot) -> TradeLotResponse:
        return TradeLotResponse(
            id=trade_lot.id,
            coin_id=trade_lot.coin_id,
            trade_status=trade_lot.trade_status,
            coin=CoinBase(name=trade_lot.coin.name, price=trade_lot.coin.price, gold=trade_lot.coin.gold, silver=trade_lot.coin.silver, bronze=trade_lot.coin.bronze),
        )

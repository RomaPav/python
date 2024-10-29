from dto.coin.coin_request import CoinBase, CoinCreate, CoinResponse
from dto.order.order_request import OrderBase
from dto.trade_lot.trade_lot_request import TradeLotBase
from model.coin import Coin
from repository.coin_repository import CoinRepository


class CoinService:
    def __init__(self, coin_repository: CoinRepository):
        self._coin_repository = coin_repository

    @staticmethod
    def validate_coin(coin: Coin) -> bool:
        if coin.name is None or coin.price is None or coin.gold is None or coin.silver is None or coin.bronze is None:
            return False
        return True

    def get(self):
        response = []
        for coin in self._coin_repository.get():
            response.append(self.coin_to_coin_response(coin))
        return response

    def add_coin(self, coin: CoinCreate):
        db_coin = Coin(**coin.dict())
        if not self.validate_coin(db_coin):
            return None
        return self.coin_to_coin_response(self._coin_repository.add_coin(db_coin))

    def update_coin(self, coin: CoinBase) -> bool:
        db_coin = Coin(**coin.dict())
        if not self.validate_coin(db_coin):
            return False
        return self._coin_repository.update_coin(db_coin)

    def delete_coin(self, id: int) -> bool:
        return self._coin_repository.delete_coin(id)

    def get_by_id(self, id: int):
        coin = self._coin_repository.get_by_id(id)
        return self.coin_to_coin_response(coin)

    def coin_to_coin_response(self,coin: Coin) -> CoinResponse:
        return CoinResponse(
            id=coin.id,
            name=coin.name,
            price=coin.price,
            gold=coin.gold,
            silver=coin.silver,
            bronze=coin.bronze,
            orders=[OrderBase(coin_id=order.coin_id, user_id=order.user_id) for order in coin.orders],
            trade_lots=[TradeLotBase(coin_id=lot.coin_id, trade_status=lot.trade_status) for lot in coin.trade_lots]
        )

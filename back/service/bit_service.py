from dto.bit.bit_request import BitResponse, BitUpdate, BitCreate
from dto.user_request import UserRequest
from dto.trade_lot.trade_lot_request import TradeLotBase
from model.bit import Bit
from repository.bit_repository import BitRepository


class BitService:
    def __init__(self, bit_repository: BitRepository):
        self._bit_repository = bit_repository

    @staticmethod
    def validate_bit(bit: Bit) -> bool:
        if bit.user_id is None or bit.trade_lot_id is None or bit.amount is None:
            return False
        return True

    def add_bit(self, bit: BitCreate):
        db_coin = Bit(**bit.dict())
        if not self.validate_bit(db_coin):
            return None
        return self._bit_repository.add_coin(db_coin)

    def update_bit(self, bit: BitUpdate) -> bool:
        db_coin = Bit(**bit.dict())
        if not self.validate_bit(db_coin):
            return False
        print(db_coin)
        return self._bit_repository.update_bit(db_coin)

    def delete_coin(self, id: int) -> bool:
        return self._bit_repository.delete_coin(id)

    def get_by_id(self, id: int):
        coin = self._bit_repository.get_by_id(id)
        return self.bit_to_bit_response(coin)

    def get_by_trade_lot_id(self, id: int):
        bit = self._bit_repository.get_by_trade_lot_id(id)
        return self.bit_to_bit_response(bit)

    def bit_to_bit_response(self, bit: Bit) -> BitResponse:
        return BitResponse(
            id=bit.id,
            user_id=bit.user_id,
            trade_lot_id=bit.trade_lot_id,
            amount=bit.amount,
            user=UserRequest(login=bit.user.login, password=bit.user.password, full_name=bit.user.full_name,
                             email=bit.user.email, role=bit.user.role) if bit.user else None,
            trade_lot=TradeLotBase(coin_id=bit.trade_lot.coin_id, trade_status=bit.trade_lot.trade_status)
        )

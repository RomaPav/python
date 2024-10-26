from dto.coin.coin_request import CoinBase
from dto.order.order_request import OrderBase, OrderCreate, OrderResponse
from dto.user_request import UserRequest
from model.order import Order
from repository.order_repository import OrderRepository


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self._order_repository = order_repository

    @staticmethod
    def validate_order(order: Order) -> bool:
        if not order.coin_id or not order.user_id:
            return False
        return True

    def get(self):
        response = []
        for order in self._order_repository.get():
            response.append(self.order_to_order_response(order))
        return response

    def add_order(self, order: OrderCreate):
        db_order = Order(**order.dict())
        if not self.validate_order(db_order):
            return None
        return self._order_repository.add_order(db_order)

    def update_order(self, order: OrderBase) -> bool:
        db_order = Order(**order.dict())
        if not self.validate_order(db_order):
            return False
        return self._order_repository.update_order(db_order)

    def delete_order(self, id: int) -> bool:
        return self._order_repository.delete_order(id)

    def get_by_user_id(self, user_id: int):
        response = []
        for order in self._order_repository.get_by_user_id(user_id):
            response.append(self.order_to_order_response(order))
        return response

    def get_by_id(self, id: int):
        return self.order_to_order_response(self._order_repository.get_by_id(id))

    def order_to_order_response(self, order: Order) -> OrderResponse:
        return OrderResponse(
            id=order.id,
            coin_id=order.coin_id,
            user_id=order.user_id,
            coin=CoinBase(name=order.coin.name, price=order.coin.price, gold=order.coin.gold, silver=order.coin.silver,
                          bronze=order.coin.bronze),
            user=UserRequest(login=order.user.login, password=order.user.password, full_name=order.user.full_name,
                             email=order.user.email,
                             role=order.user.role),
        )

from database.database import SessionLocal
from model.order import Order


class OrderRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get(self):
        return self.db.query(Order).all()

    def add_order(self, order: Order):
        self.db.add(order)
        self.db.commit()
        return True

    def delete_order(self, id: int):
        self.db.query(Order).filter(Order.id == id).delete()
        return True

    def get_by_user_id(self, user_id: int):
        return self.db.query(Order).filter(Order.user_id == user_id).all()

    def get_by_id(self, id: int) -> Order:
        return self.db.query(Order).filter(Order.id == id).first()

    def update_order(self, order: Order):
        try:
            rows_affected = self.db.query(Order).filter(Order.id == order.id).update({
                'coin_id': order.coin_id,
                'user_id': order.user_id,
            })

            if rows_affected == 0:
                raise ValueError(f"TradeLot with id {order.id} not found.")

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return True
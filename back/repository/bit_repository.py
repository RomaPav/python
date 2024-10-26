from database.database import SessionLocal
from model.bit import Bit


class BitRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_coin(self, bit: Bit):
        self.db.add(bit)
        self.db.commit()
        return True

    def delete_coin(self, id: int):
        self.db.query(Bit).filter(Bit.id == id).delete()
        return True

    def get_by_id(self, id: int) -> Bit:
        return self.db.query(Bit).filter(Bit.id == id).first()

    def get_by_trade_lot_id(self, id: int) -> Bit:
        return self.db.query(Bit).filter(Bit.trade_lot_id == id).first()

    def update_bit(self, bit: Bit):
        try:
            rows_affected = self.db.query(Bit).filter(Bit.id == bit.id).update({
                'user_id': bit.user_id,
                'trade_lot_id': bit.trade_lot_id,
                'amount': bit.amount,
            })

            if rows_affected == 0:
                raise ValueError(f"Bit with id {bit.id} not found.")

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return True

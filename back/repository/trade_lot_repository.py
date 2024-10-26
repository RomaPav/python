from sqlalchemy import or_

from database.database import SessionLocal
from model.trade_lot import TradeLot


class TradeLotRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get(self):
        return self.db.query(TradeLot).all()

    def add_trade_lot(self, trade_lot: TradeLot):
        self.db.add(trade_lot)
        self.db.commit()
        return True

    def delete_trade_lot(self, id: int):
        self.db.query(TradeLot).filter(TradeLot.id == id).delete()
        return True

    def get_by_coin_id(self, coin_id: int):
        return self.db.query(TradeLot).filter(TradeLot.coin_id == coin_id).all()

    def get_by_id(self, id: int):
        return self.db.query(TradeLot).filter(TradeLot.id == id).first()

    def active_trade_lot(self):
        return self.db.query(TradeLot).filter(
            or_(TradeLot.trade_status == 'STARTED', TradeLot.trade_status == 'NOT_STARTED')
        ).all()

    def active_trade_lot_for_buying(self):
        return self.db.query(TradeLot).filter(TradeLot.trade_status == 'STARTED').all()

    def update_trade_lot(self, trade_lot: TradeLot):
        try:
            rows_affected = self.db.query(TradeLot).filter(TradeLot.id == trade_lot.id).update({
                'coin_id': trade_lot.coin_id,
                'trade_status': trade_lot.trade_status,
            })

            if rows_affected == 0:
                raise ValueError(f"TradeLot with id {trade_lot.id} not found.")

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return True

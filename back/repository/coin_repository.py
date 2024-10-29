from database.database import SessionLocal
from model.coin import Coin


class CoinRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get(self):
        return self.db.query(Coin).all()

    def add_coin(self, coin: Coin):
        self.db.add(coin)
        self.db.commit()
        return coin

    def delete_coin(self, id: int):
        self.db.query(Coin).filter(Coin.id == id).delete()
        return True

    def get_by_id(self, id: int) -> Coin:
        return self.db.query(Coin).filter(Coin.id == id).first()

    def update_coin(self, coin: Coin):
        try:
            rows_affected = self.db.query(Coin).filter(Coin.id == coin.id).update({
                'name': coin.name,
                'price': coin.price,
                'gold': coin.gold,
                'silver': coin.silver,
                'bronze': coin.bronze,
            })

            if rows_affected == 0:
                raise ValueError(f"Coin with id {coin.id} not found.")

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return True
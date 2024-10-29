from database.database import SessionLocal
from model.user import User


class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        return True

    def delete_user(self, user: User):
        user.is_active = False
        self.update_user(user)
        return True

    def get_user_by_login_and_password(self, user: User) -> User:
        return self.db.query(User).filter(User.login == user.login and User.password == user.password).one_or_none()

    def get_by_login(self, login: str) -> User:
        return self.db.query(User).filter(User.login == login).first()

    def get_by_id(self, id: int) -> User:
        return self.db.query(User).filter(User.id == id).first()

    def update_user(self, user: User):
        # user_updated = self.db.query(User).filter(User.id == user.id).one_or_none()
        # user_updated.update({
        #     'login': user.login,
        #     'password': user.password,
        #     'is_active': user.is_active,
        # })
        # self.db.commit()

        try:
            rows_affected = self.db.query(User).filter(User.id == user.id).update({
                'login': user.login,
                'full_name': user.full_name,
                'email': user.email,
                'password': user.password,
                'role': user.role,
                'is_active': user.is_active,
            })

            if rows_affected == 0:
                raise ValueError(f"User with id {user.id} not found.")

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return True

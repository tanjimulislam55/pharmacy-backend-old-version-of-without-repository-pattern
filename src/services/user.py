from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import UserCreate, User, UserUpdate
from models import Users, Roles
from utils.auth import get_password_hash

class UserService():

    def create(self, db_in: UserCreate, db: Session) -> User:
        default_role = db.query(Roles).filter(Roles.rolename == "employee").first()
        db_obj = Users(
            **db_in.dict(exclude={"password"}), role_id=default_role.id, 
            hashed_password=get_password_hash(db_in.password)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_email(self, email: str, db: Session) -> Optional[Users]:
        return db.query(Users).filter(Users.email == email).first()

    def get_by_username(self, username: str, db: Session) -> Optional[Users]:
        return db.query(Users).filter(Users.username == username).first()

    # def update(self, db_in: UserUpdate) -> User:
    #     db_obj = Users(**db_in.dict())
    #     self.db.add(db_obj)
    #     self.db.commit()
    #     self.db.refresh(db_obj)
    #     return db_obj

    def get_many(self, db: Session) -> List[User]:
        return db.query(Users).all()

    def get_one(self, id: int, db: Session) -> User:
        return db.query(Users).filter(Users.id == id).first()
        


user_service = UserService()
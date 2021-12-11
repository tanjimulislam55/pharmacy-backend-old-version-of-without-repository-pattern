from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import UserCreate, User, UserUpdate
from models import Users, Roles
from utils.auth import get_password_hash

class UserService():

    def create(self, db_in: UserCreate, db: Session) -> User:
        db_obj = Users(
            **db_in.dict(exclude={"password"}),
            deactivated=True,
            password=get_password_hash(db_in.password)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_email(self, email: str, db: Session) -> Optional[Users]:
        return db.query(Users).filter(Users.email == email).first()

    def get_by_username(self, username: str, db: Session) -> Optional[Users]:
        return db.query(Users).filter(Users.username == username).first()

    def update(self, user_id: int, db_in: UserUpdate, db: Session) -> Optional[User]:
        db.query(Users).filter(Users.id == user_id).update(
            db_in.dict(exclude_unset=True), synchronize_session="evaluate"
        )
        db.commit()
        return db.query(Users).filter(Users.id == user_id).first()

    def update_role(self, user_id: int, role_id: int, db: Session) -> Optional[User]:      
        db.query(Users).filter(Users.id == user_id).update(
            {Users.role_id: role_id}, synchronize_session=False
        )
        db.commit()
        return db.query(Users).filter(Users.id == user_id).first()

    def get_many(self, db: Session) -> List[Users]:
        return db.query(Users).all()

    def get_one(self, id: int, db: Session) -> Optional[User]:
        return db.query(Users).filter(Users.id == id).first()
        


user_service = UserService()
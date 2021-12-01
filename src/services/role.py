from typing import List, Optional
from sqlalchemy.orm.session import Session

from schemas import Role, RoleCreate, RoleUpdate
from models import Roles

class RoleService():

    def create(self, db_in: RoleCreate, db: Session) -> Role:
        db_obj = Roles(**db_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(self, db_in: RoleUpdate, db: Sesssion) -> Role:
    #     db_obj = Roles(**db_in.dict())
    #     self.db.add(db_obj)
    #     self.db.commit()
    #     self.db.refresh(db_obj)
    #     return db_obj

    def get_many(self, db: Session) -> List[Role]:
        return db.query(Roles).all()
        

role_service = RoleService()
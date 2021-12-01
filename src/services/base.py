from typing import Optional
from sqlalchemy.orm.session import Session

import models
import schemas


class DBBaseMixin():
    def __init__(self, db: Session) -> None:
        self.db = db


class BaseService(DBBaseMixin):

    def create(self, db: Session, db_in: schemas.UserCreate):
        pass

    def get_one(self):
        pass

    def get_many(self):
        pass 

    def get_by_email(self, db: Session, email: str):
        pass 

    def update(self):
        pass

    def remove(self):
        pass
    



from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import Type, TypeCreate
from models import Types

class TypeService():

    def create(self, db_in: TypeCreate, db: Session) -> Type:
        db_obj = Types(**db_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_name(self, name: str, db: Session) -> Optional[Types]:
        return db.query(Types).filter(Types.name == name).first()

    def get_many(self, db: Session) -> List[Types]:
        return db.query(Types).all()
        
    def delete(self, id: int, db: Session):
        if not db.query(Types).filter(Types.id == id).first():
            return f"Type not found for id {id}"
        return db.query(Types).filter(Types.id == id).delete(synchronize_session='evaluate')

type_service = TypeService()
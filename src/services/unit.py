from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import Unit, UnitCreate
from models import Units

class UnitService():

    def create(self, db_in: UnitCreate, db: Session) -> Unit:
        db_obj = Units(**db_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_name(self, name: str, db: Session) -> Optional[Units]:
        return db.query(Units).filter(Units.name == name).first()

    def get_many(self, db: Session) -> List[Units]:
        return db.query(Units).all()

    def delete(self, id: int, db: Session):
        if not db.query(Units).filter(Units.id == id).first():
            return f"Unit not found for id {id}"
        return db.query(Units).filter(Units.id == id).delete(synchronize_session='evaluate')
        
    def update(self, id: int, name: str, db: Session) -> Optional[Units]:
        db.query(Units).filter(Units.id == id).update(
            {Units.name: name}, synchronize_session=False
        )
        db.commit()
        return db.query(Units).filter(Units.id == id).first()


unit_service = UnitService()
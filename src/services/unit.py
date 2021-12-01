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

    def get_many(self, db: Session) -> List[Unit]:
        return db.query(Units).all()
        


unit_service = UnitService()
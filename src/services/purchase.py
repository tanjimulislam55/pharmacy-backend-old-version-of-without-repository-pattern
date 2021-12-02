from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import PurchaseCreate, PurchaseLineCreate, Purchase
from models import Purchases, PurchaseLines
from services import medicine_service

class PurchaseService():

    def create(self, db_in: PurchaseCreate, db_in_line: PurchaseLineCreate, db: Session) -> Purchase:
        db_obj = Purchases(**db_in.dict())
        db.add(db_obj)
        db.flush()
        # checking medicine from db
        db_obj_line = [PurchaseLines(**each_line.dict(), purchase_id=db_obj.id) for each_line in db_in_line]
        try:
            for line in db_obj_line:
                if not medicine_service.get_one(line.medicine_id, db):
                    return f"No medicine found for id {line.medicine_id}"
                db.add(line)
                if line.received_qty > 0:
                    medicine_service.update_to_increase_stock(line.medicine_id, line.received_qty, db)
        except:
            return "Problem occured during adding purchase lines"
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_many(self, db: Session) -> List[Purchase]:
        return db.query(Purchases).all()

    def get_one(self, db: Session) -> Purchase:
        db.query(Purchases).filter(Purchases.id == id).first()
        


purchase_service = PurchaseService()
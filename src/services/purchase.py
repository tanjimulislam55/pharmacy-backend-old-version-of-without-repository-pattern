from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import PurchaseCreate, PurchaseLineCreate, Purchase, BillLineCreate, PurchaseLine
from models import Purchases, PurchaseLines
from services import medicine_service

class PurchaseService():

    def create(self, db_in: PurchaseCreate, db_in_line: PurchaseLineCreate, db: Session) -> Purchase:
        db_obj = Purchases(**db_in.dict())
        db.add(db_obj)
        db.flush()
        db_obj_line = [PurchaseLines(**each_line.dict(), purchase_id=db_obj.id) for each_line in db_in_line]
        try:
            for line in db_obj_line:
                # checking medicine from db
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

    def get_many(self, db: Session) -> List[Purchases]:
        return db.query(Purchases).all()

    def get_one(self, id: int, db: Session) -> Optional[Purchases]:
        return db.query(Purchases).filter(Purchases.id == id).first()

    def update_sold_qty(self, id: int, value: int, db: Session):
        db.query(PurchaseLines).filter(PurchaseLines.id == id).update(
            {PurchaseLines.sold_qty: PurchaseLines.sold_qty + value}, synchronize_session=False
        )
        db.commit()
    
    def salable_purchase_lines(self, medicine_id: int, db: Session) -> Optional[List[PurchaseLines]]:
        return db.query(PurchaseLines).filter(
            PurchaseLines.received_qty - PurchaseLines.sold_qty > 0,
            PurchaseLines.medicine_id == medicine_id
        ).order_by(PurchaseLines.purchase_id.asc()).all()

    def has_available_qty(self, db_in_line: BillLineCreate, db: Session) -> bool:
        for each_db_in_line in db_in_line:
            purchase_lines_on_medicine_id = db.query(PurchaseLines).filter(
                PurchaseLines.medicine_id == each_db_in_line.medicine_id
            ).all()
            total_available_qty = sum([(line.received_qty-line.sold_qty) for line in purchase_lines_on_medicine_id])
            if total_available_qty > each_db_in_line.qty:
                return True


purchase_service = PurchaseService()
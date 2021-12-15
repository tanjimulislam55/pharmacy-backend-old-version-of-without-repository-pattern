from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import BillLine, BillLineCreate, BillCreate, Bill
from models import BillLines, Bills
from services import medicine_service, purchase_service

class BillService():

    def create(self, db_bill_in: BillCreate, db_bill_line_in: BillLineCreate, db: Session) -> Bill:
        db_obj = Bills(**db_bill_in.dict())
        db.add(db_obj)
        db.flush()

        for each_db_bill_line in db_bill_line_in:
            qty = each_db_bill_line.qty
            profit: float = 0
            for each_purchase_line in purchase_service.salable_purchase_lines(each_db_bill_line.medicine_id, db):
                if qty > 0:
                    if not each_db_bill_line.price: # 0 returns False
                        retail_price = medicine_service.get_retail_price(each_purchase_line.medicine_id, db)
                    retail_price = each_db_bill_line.price
                    salable_medicine_qty = each_purchase_line.received_qty - each_purchase_line.sold_qty
                    if salable_medicine_qty >= qty:
                        # updating sold_qty of purchase_lines table
                        purchase_service.update_sold_qty(each_purchase_line.id, qty, db)
                        # updating medicine stock
                        medicine_service.update_to_dicrease_stock(each_purchase_line.medicine_id, qty, db)
                        # -------------------------------------------------------------------------
                        profit += ((retail_price - each_purchase_line.purchase_price) * qty)
                        break
                    else:
                        # updating sold_qty of purchase_lines table
                        purchase_service.update_sold_qty(each_purchase_line.id, salable_medicine_qty, db)
                        # updating medicine stock
                        medicine_service.update_to_dicrease_stock(each_purchase_line.medicine_id, salable_medicine_qty, db)
                        # -------------------------------------------------------------------------
                        qty = qty - salable_medicine_qty
                        profit += ((retail_price - each_purchase_line.purchase_price) * salable_medicine_qty)
            db_obj_line = BillLines(**each_db_bill_line.dict(), bill_id=db_obj.id, profit_per_bill=profit)
            db.add(db_obj_line)
            db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_many(self, db: Session) -> List[Bills]:
        return db.query(Bills).all()

    def get_one(self, id: int, db: Session) -> Optional[Bills]:
        return db.query(Bills).filter(Bills.id == id).first()
        


bill_service = BillService()
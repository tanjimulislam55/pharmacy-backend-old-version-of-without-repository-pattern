from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import Medicine, MedicineCreate, MedicineDetailUpdate, MedicineDetail, MedicineDetailCreate
from models import Medicines, MedicineDetails

class MedicineService():

    def create(self, db_in: MedicineCreate, db: Session) -> Medicine:
        db_obj_medicine = Medicines(**db_in.dict())
        db.add(db_obj_medicine)
        db.flush()
        # also assigning to detail table
        db_obj_medicine_detail = MedicineDetails(medicine_id=db_obj_medicine.id)
        db.add(db_obj_medicine_detail)
        db.commit()
        db.refresh(db_obj_medicine)
        return db_obj_medicine

    def get_by_name(self, name: str, db: Session) -> Optional[Medicines]:
        return db.query(Medicines).filter(Medicines.name == name).first()

    def update(self, medicine_id: int, db_in: MedicineDetailUpdate, db: Session) -> Medicine:
        db.query(MedicineDetails).filter(
            MedicineDetails.medicine_id == medicine_id
        ).update(
            db_in.dict(), synchronize_session="evaluate"
        )
        db.commit()
        return db.query(MedicineDetails).filter(MedicineDetails.medicine_id == medicine_id).first()
    
    def update_to_increase_stock(self, medicine_id: int, value: int, db: Session) -> Optional[Medicine]:
        db.query(MedicineDetails).filter(
            MedicineDetails.medicine_id == medicine_id
        ).update(
            {MedicineDetails.stock: MedicineDetails.stock + value}, synchronize_session=False
        )
        db.commit()
    
    def update_to_dicrease_stock(self, medicine_id: int, value: int, db: Session) -> Optional[Medicine]:
        db.query(MedicineDetails).filter(
            MedicineDetails.medicine_id == medicine_id
        ).update(
            {MedicineDetails.stock: MedicineDetails.stock - value}, synchronize_session=False
        )
        db.commit()

    def get_many(self, db: Session) -> List[Medicine]:
        return db.query(Medicines).all()

    def get_one(self, id: int, db: Session) -> Medicine:
        return db.query(Medicines).filter(Medicines.id == id).first()

    def get_retail_price(self, id: int, db: Session) -> int:
        medicine_detail = db.query(MedicineDetails).filter(MedicineDetails.medicine_id == id).first()
        return medicine_detail.retail_price
        


medicine_service = MedicineService()
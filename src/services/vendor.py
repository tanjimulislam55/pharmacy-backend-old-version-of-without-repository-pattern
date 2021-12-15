from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import VendorCreate, Vendor, VendorUpdate
from models import Vendors

class VendorService():

    def create(self, db_in: VendorCreate, db: Session) -> Vendor:
        db_obj = Vendors(**db_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_name(self, name: str, db: Session) -> Optional[Vendors]:
        return db.query(Vendors).filter(Vendors.name == name).first()

    def get_by_mobile(self, mobile: str, db: Session) -> Optional[Vendors]:
        return db.query(Vendors).filter(Vendors.mobile == mobile).first()

    def update(self, vendor_id: int, db_in: VendorUpdate, db: Session) -> Optional[Vendors]:
        db.query(Vendors).filter(Vendors.id == vendor_id).update(
            db_in.dict(exclude_unset=True), synchronize_session="evaluate"
        )
        db.commit()
        return db.query(Vendors).filter(Vendors.id == vendor_id).first()

    def get_many(self, db: Session) -> List[Vendors]:
        return db.query(Vendors).all()

    def get_one(self, id: int, db: Session) -> Optional[Vendors]:
        return db.query(Vendors).filter(Vendors.id == id).first()
        


vendor_service = VendorService()
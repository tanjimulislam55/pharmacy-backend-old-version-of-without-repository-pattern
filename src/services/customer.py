from typing import List, Optional
from pydantic.networks import EmailStr
from sqlalchemy.orm.session import Session

from schemas import CustomerCreate, CustomerUpdate, Customer
from models import Customers

class CustomerService():

    def create(self, db_in: CustomerCreate, db: Session) -> Customer:
        print(db_in.dict())
        db_obj = Customers(**db_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_many(self, db: Session) -> List[Customers]:
        return db.query(Customers).all()

    def get_one(self, id: int, db: Session) -> Optional[Customer]:
        return db.query(Customers).filter(Customers.id == id).first()

    def get_by_phone(self, phone: str, db: Session) -> Optional[Customer]:
        return db.query(Customers).filter(Customers.phone == phone).first()

    def get_by_email(self, email: EmailStr, db: Session) -> Optional[Customer]:
        return db.query(Customers).filter(Customers.email == email).first()

    def delete(self, id: int, db: Session):
        if not db.query(Customers).filter(Customers.id == id).first():
            return f"Customer not found for id {id}"
        db.query(Customers).filter(Customers.id == id).delete(synchronize_session="evaluate")
        db.commit()

    def update(self, customer_id: int, db_in: CustomerUpdate, db: Session) -> Optional[Customers]:
        db.query(Customers).filter(
            Customers.id == customer_id
        ).update(
            db_in.dict(exclude_unset=True), synchronize_session="evaluate"
        )
        db.commit()
        return db.query(Customers).filter(Customers.id == customer_id).first()
    


customer_service = CustomerService()
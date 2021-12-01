from typing import Optional, List
from sqlalchemy.orm.session import Session

from schemas import CategoryCreate, Category
from models import Categories

class CategoryService():

    def create(self, db_in: CategoryCreate, db: Session) -> Category:
        db_obj = Categories(**db_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_name(self, name: str, db: Session) -> Optional[Categories]:
        return db.query(Categories).filter(Categories.name == name).first()

    def get_many(self, db: Session) -> List[Category]:
        return db.query(Categories).all()
        


category_service = CategoryService()
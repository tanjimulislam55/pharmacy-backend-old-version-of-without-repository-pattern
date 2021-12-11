from typing import Optional
from pydantic import BaseModel


class MedicineDetailCreate(BaseModel):
    retail_price: Optional[float] = None
    stock: Optional[int] = 0
    medicine_id: int


class MedicineDetail(MedicineDetailCreate):
    id: int

    class Config:
        orm_mode = True


class MedicineDetailUpdate(BaseModel):
    retail_price: Optional[float] = None
    stock: Optional[int] = None


class MedicineCreate(BaseModel):
    name: str
    vendor_id: int
    unit_id: int
    type_id: int
    category_id: int


class Medicine(MedicineCreate):
    id: int
    medicine_detail: Optional[MedicineDetail] = None

    class Config:
        orm_mode = True


class TypeCreate(BaseModel):
    name: str


class Type(TypeCreate):
    id: int

    class Config:
        orm_mode = True


class TypeDelete(BaseModel):
    id: int


class UnitCreate(BaseModel):
    name: str


class Unit(UnitCreate):
    id: int

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    name: str


class Category(CategoryCreate):
    id: int

    class Config:
        orm_mode = True




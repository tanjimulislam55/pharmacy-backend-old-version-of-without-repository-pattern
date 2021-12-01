from pydantic import BaseModel
from pydantic.networks import EmailStr


class VendorCreate(BaseModel):
    name: str 
    email: EmailStr
    mobile: str


class VendorUpdate(VendorCreate):
    pass


class Vendor(VendorCreate):
    id: int

    class Config:
        orm_mode = True



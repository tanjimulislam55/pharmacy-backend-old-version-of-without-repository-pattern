from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from db.config import Base



class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rolename = Column(String(20), default="employee")

    users = relationship("Users", back_populates="role")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255))
    deactivated = Column(Boolean, nullable=False, default=True)

    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Roles", back_populates="users")


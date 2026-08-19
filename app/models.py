from enum import Enum as PyEnumClass

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class UserRole(PyEnumClass):
    ADMIN = "admin"
    CASHIER = "cashier"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(length=50), unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String(length=50), nullable=False)

    role = Column(Enum(UserRole), default=UserRole.CASHIER, nullable=False)

    checks_table = relationship("Checks", back_populates="cashier")


class Drugs(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=40), nullable=False)
    amount = Column(Integer, default=0)
    desc = Column(Text, nullable=False)
    base_price = Column(Float, default=0)
    cell_price = Column(Float, default=0)
    bar_code = Column(String(length=20))

    item_table = relationship("CheckItem", back_populates="drug")


class Checks(Base):
    __tablename__ = "checks"

    id = Column(Integer, primary_key=True, nullable=False)
    check_num = Column(String, unique=True, nullable=False)
    date_created = Column(DateTime, nullable=False)
    cashier_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    cashier = relationship("Users", back_populates="checks_table")
    item_table = relationship("CheckItem", back_populates="check")


class CheckItem(Base):
    __tablename__ = "checkitem"

    id = Column(Integer, primary_key=True, nullable=False)
    amount = Column(Integer, default=1)
    drug_id = Column(Integer, ForeignKey("drugs.id"), nullable=False)
    check_id = Column(Integer, ForeignKey("checks.id"), nullable=False)

    drug = relationship("Drugs", back_populates="item_table")
    check = relationship("Checks", back_populates="item_table")

from pydantic import BaseModel

from app.models import UserRole


class UsersBase(BaseModel):
    username: str
    password: str
    full_name: str
    role: UserRole = UserRole.CASHIER


class Admin(BaseModel):
    username: str
    password: str
    full_name: str
    role: UserRole = UserRole.ADMIN

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    full_name: str | None = None
    role: UserRole | None = None


class DrugsBase(BaseModel):
    name: str
    amount: int
    desc: str
    base_price: float
    cell_price: float


class DrugUpdate(BaseModel):
    name: str | None = None
    amount: int | None = None
    desc: str | None = None
    base_price: float | None = None
    cell_price: float | None = None


class DrugAmountUpdate(BaseModel):
    id: int
    amount: int


class ChecksBase(BaseModel):
    cashier_id: int



class CheckItemBase(BaseModel):
    amount: int
    drug_id: int
    check_id: int

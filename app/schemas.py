from datetime import datetime

from pydantic import BaseModel

from app.models import UserRole


class UsersBase(BaseModel):
    username: str
    password: str
    full_name: str
    role: UserRole = UserRole.CASHIER


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
    bar_code: str


class ChecksBase(BaseModel):
    check_num: str
    date_created: datetime
    cashier_id: int


class CheckItemBase(BaseModel):
    amount: int
    drug_id: int
    check_id: int

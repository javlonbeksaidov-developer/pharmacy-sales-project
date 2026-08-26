from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CheckItem, Checks, Users
from app.schemas import CheckReturn, ItemData, ItemsOut

sale_router = APIRouter(tags=["Sale router"])


@sale_router.post("/sales/open-check/", response_model=CheckReturn)
def open_check(_cashier_id: int, db: Session = Depends(get_db)):  # noqa: B008
    cashier = db.query(Users).filter(Users.id == _cashier_id).first()
    if cashier is None:
        raise HTTPException(status_code=404, detail="Cashier not found")

    date = datetime.now()  # noqa: DTZ005
    check = Checks(
        check_num=f"Check - {date}",
        date_created=date,
        cashier_id=_cashier_id,
        status=True,
    )
    db.add(check)
    db.commit()
    db.refresh(check)
    return check


@sale_router.post("/sales/add-item-to-check/", response_model=ItemsOut)
def add_item(item_data: ItemData, _cashier_id: int, db: Session = Depends(get_db)):  # noqa: B008
    cashier = db.query(Users).get(_cashier_id)

    if cashier is None or cashier.role.value != "cashier":
        raise HTTPException(status_code=401, detail="Mumkin emas !")

    item = (
        db.query(CheckItem)
        .filter(CheckItem.check_id == item_data.check_id)
        .filter(CheckItem.drug_id== item_data.drug_id)
        .first()
    )
    if item is not None:
        item.amount += item_data.amount
        db.commit()
    else:
        item = CheckItem(
            amount=item_data.amount,
            drug_id=item_data.drug,
            check_id=item_data.check_id,
        )

        db.add(item)
        db.commit()

    db.refresh(item)
    return item


@sale_router.post("/sales/remove-item/{check_id}/{item_id}")
def remove_item(cashier_: int, check_id: int, item_id: int, db=Depends(get_db)):  # noqa: B008
    cashier = db.query(Users).get(cashier_)

    if cashier is None or cashier.role.value != "cashier":
        raise HTTPException(status_code=401, detail="Mumkin emas !")

    check = db.query(Checks).get(check_id)
    item = db.query(CheckItem).get(item_id)

    if check is None or check.cashier_id != cashier_:
        raise HTTPException(status_code=404, detail="Check topilmadi!")

    if item is None:
        raise HTTPException(status_code=404, detail="Check Item topilmadi!")

    if item.amount <= 1:
        db.delete(item)
        db.commit()
        return {"message": "Item Deleted !"}
    else:
        item.amount -= 1
        db.commit()
        db.refresh(item)

    return item


@sale_router.get("/sales/sales-all/", response_model=list[CheckReturn])
def get_checks(admin_id: int, db=Depends(get_db)):  # noqa: B008
    cashier = db.query(Users).get(admin_id)

    if cashier is None or cashier.role.value != "admin":
        raise HTTPException(status_code=401, detail="Mumkin emas !")

    sales = db.query(Checks).all()

    return sales

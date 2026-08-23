from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CheckItem, Users
from app.schemas import CheckItemBase

check_item_router = APIRouter(tags=["Check Item router"])

""" POST """


@check_item_router.post("/check-items/create/")
def create_check_item(admin_id: int, item: CheckItemBase, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role.value != "admin":
        print(admin.role)
        raise HTTPException(status_code=401, detail="Return 1 around")

    new_check_item = CheckItem(**item.model_dump())
    db.add(new_check_item)
    db.commit()
    db.refresh(new_check_item)
    return new_check_item


""" GET """


@check_item_router.get("/check-items/")
def get_all_check_items(user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    check_item = db.query(CheckItem).all()
    return check_item


@check_item_router.get("/check-items/{check_item_id}")
def get_check_item_by_id(user_id: int, check_item_id: int, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    check_item = db.query(CheckItem).filter(CheckItem.id == check_item_id).first()
    return check_item


""" PUT """


@check_item_router.put("/check-items/update/{check_item_id}")
def update_check(admin_id: int, check_item_id: int, check_item: CheckItemBase, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role != "ADMIN":
        raise HTTPException(status_code=401, detail="Return 1 around")

    db_check_item = db.query(CheckItem).filter(CheckItem.id == check_item_id).first()

    if not db_check_item:
        return {"message": "Check not found"}

    db_check_item.amount = check_item.amount
    db_check_item.drug_id = check_item.drug_id
    db_check_item.check_id = check_item.check_id

    db.commit()
    db.refresh(db_check_item)
    return db_check_item


""" DELETE """


@check_item_router.delete("/check-items/delete/{check_item_id}")
def delete_check(admin_id: int, check_item_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role != "ADMIN":
        raise HTTPException(status_code=401, detail="Return 1 around")

    db_check = db.query(CheckItem).filter(CheckItem.id == check_item_id).first()

    if not db_check:
        return {"message": "Check not found"}

    db.delete(db_check)
    db.commit()
    return {"message": "Check deleted"}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CheckItem
from app.schemas import CheckItemBase

check_item_router = APIRouter()

""" POST """


@check_item_router.post("/check-items/create/")
def create_check_item(item: CheckItemBase, db: Session = Depends(get_db)):  # noqa: B008
    new_check_item = CheckItem(
        amount=item.amount,
        drug_id=item.drug_id,
        check_id=item.check_id,
    )
    db.add(new_check_item)
    db.commit()
    db.refresh(new_check_item)
    return new_check_item


""" GET """


@check_item_router.get("/check-items/")
def get_all_check_items(db: Session = Depends(get_db)):  # noqa: B008
    check_item = db.query(CheckItem).all()
    return check_item


@check_item_router.get("/check-items/{check_item_id}")
def get_check_item_by_id(check_item_id: int, db: Session = Depends(get_db)):  # noqa: B008
    check_item = db.query(CheckItem).filter(CheckItem.id == check_item_id).first()
    return check_item


""" PUT """


@check_item_router.put("/check-items/update/{check_item_id}")
def update_check(check_item_id: int, check_item: CheckItemBase, db: Session = Depends(get_db)):  # noqa: B008
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
def delete_check(check_item_id: int, check: CheckItemBase, db: Session = Depends(get_db)):  # noqa: B008
    db_check = db.query(CheckItem).filter(CheckItem.id == check_item_id).first()

    if not db_check:
        return {"message": "Check not found"}

    db.delete(db_check)
    db.commit()
    return {"message": "Check deleted"}

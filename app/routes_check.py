from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Checks
from app.schemas import ChecksBase

check_router = APIRouter(tags=["Check router"])

""" POST """


@check_router.post("/checks/create/")
def create_check(item: ChecksBase, db: Session = Depends(get_db)):  # noqa: B008
    new_check = Checks(**item.model_dump())
    db.add(new_check)
    db.commit()
    db.refresh(new_check)
    return new_check


""" GET """


@check_router.get("/checks/")
def get_all_checks(db: Session = Depends(get_db)):  # noqa: B008
    checks = db.query(Checks).all()
    return checks


@check_router.get("/checks/{check_id}")
def get_check_by_id(check_id: int, db: Session = Depends(get_db)):  # noqa: B008
    checks = db.query(Checks).filter(Checks.id == check_id).first()
    return checks


""" PUT """


@check_router.put("/checks/update/{check_id}")
def update_check(check_id: int, check: ChecksBase, db: Session = Depends(get_db)):  # noqa: B008
    db_check = db.query(Checks).filter(Checks.id == check_id).first()

    if not db_check:
        return {"message": "Check not found"}

    db_check.check_num = check.check_num
    db_check.date_created = check.date_created
    db_check.cashier_id = check.cashier_id

    db.commit()
    db.refresh(db_check)
    return db_check


""" DELETE """


@check_router.delete("/checks/delete/{check_id}")
def delete_check(check_id: int, check: ChecksBase, db: Session = Depends(get_db)):  # noqa: B008
    db_check = db.query(Checks).filter(Checks.id == check_id).first()

    if not db_check:
        return {"message": "Check not found"}

    db.delete(db_check)
    db.commit()
    return {"message": "Check deleted"}

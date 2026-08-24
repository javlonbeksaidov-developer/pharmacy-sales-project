from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Checks, Users
from app.schemas import CheckReturn

sale_router = APIRouter(tags=["Sale router"])

""" POST """


@sale_router.post("/open-check/", response_class=CheckReturn)
def open_check(_cashier_id: int, db: Session = Depends(get_db)):  # noqa: B008
    cashier = db.query(Users).filter(Users.id == _cashier_id).first()
    if cashier is None:
        raise HTTPException(status_code=404, detail="Cashier not found")

    date = datetime.now()  # noqa: DTZ005
    check = Checks(
        check_num = f"Check - {date}",
        date_created = date,
        cashier_id = _cashier_id,
        status = True,
    )
    db.add(check)
    db.commit()
    db.refresh(check)
    return check

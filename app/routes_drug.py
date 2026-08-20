from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Drugs, Users
from app.schemas import DrugsBase

drug_router = APIRouter(tags=["Drug router"])

""" POST """


@drug_router.post("/drugs/create/")
def create_drug(admin_id:int, drug: DrugsBase, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        new_drug = Drugs(**drug.model_dump())
        db.add(new_drug)
        db.commit()
        db.refresh(new_drug)
        return new_drug
    else:
        return {"message": "return 1 around!"}


""" GET """


@drug_router.get("/drugs/")
def get_all_drugs(admin_id:int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        drug = db.query(Drugs).all()
        return drug
    else:
        return {"message": "return 1 around!"}


@drug_router.get("/drugs/{drug_id}")
def get_drug_by_id(admin_id:int, drug_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        drug = db.query(Drugs).filter(Drugs.id == drug_id).first()
        return drug
    else:
        return {"message": "return 1 around!"}


""" PUT """


@drug_router.put("/drugs/update/{drug_id}")
def update_drug(admin_id: int, drug_id: int, drug: DrugsBase, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_drug = db.query(Drugs).filter(Drugs.id == drug_id).first()

        if not db_drug:
            return {"message": "Drug not found"}

        db_drug.name = drug.name
        db_drug.amount = drug.amount
        db_drug.desc = drug.desc
        db_drug.base_price = drug.base_price
        db_drug.cell_price = drug.cell_price
        db_drug.bar_code = drug.bar_code

        db.commit()
        db.refresh(db_drug)
        return db_drug
    else:
        return {"message": "return 1 around!"}


""" DELETE """


@drug_router.delete("/drugs/delete/{drug_id}")
def delete_drug(admin_id: int, drug_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_drug = db.query(Drugs).filter(Drugs.id == drug_id).first()

        if not db_drug:
            return {"message": "Drug not found"}

        db.delete(db_drug)
        db.commit()
        return {"message": "Drug was deleted"}
    else:
        return {"message": "return 1 around!"}

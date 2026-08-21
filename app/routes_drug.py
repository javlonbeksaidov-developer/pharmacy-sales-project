from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Drugs, Users
from app.schemas import DrugAmountUpdate, DrugsBase, DrugUpdate

drug_router = APIRouter(tags=["Drug router"])

""" POST """


@drug_router.post("/drugs/create/")
def create_drug(admin_id: int, drug: DrugsBase, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()

    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role.value == "admin":
        new_drug = Drugs(**drug.model_dump())
        db.add(new_drug)
        db.commit()

        new_drug.bar_code = f"{new_drug.id} - {new_drug.name}"
        db.commit()
        db.refresh(new_drug)
        return {"message": "created", "success": True, "data": new_drug}
    else:
        return {"message": "return 1 around!"}


""" GET """


@drug_router.get("/drugs/")
def get_all_drugs(user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(Users).filter(Users.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    drugs = db.query(Drugs).all()

    return {"message": "get_all", "success": True, "data": drugs}    


@drug_router.get("/drugs/{drug_id}")
def get_drug_by_id(user_id: int, drug_id: int, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(Users).filter(Users.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    drug = db.query(Drugs).filter(Drugs.id == drug_id).first()

    if drug is None:
        raise HTTPException(status_code=404, detail="Drug not found")

    return {"message": "get_by_id", "success": True, "data": drug}


""" PUT """


@drug_router.put("/drugs/update/{drug_id}")
def update_drug(admin_id: int, drug_id: int, drug: DrugUpdate, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()

    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role.value == "admin":
        db_drug = db.query(Drugs).filter(Drugs.id == drug_id).first()

        if db_drug is None:
            raise HTTPException(status_code=404, detail="Drug not found")

        updated_drug = drug.model_dump(exclude_unset=True)

        for key, value in updated_drug.items():
            setattr(db_drug, key, value)

        db.commit()
        db.refresh(db_drug)
        return {"message": "updated", "success": True, "data": db_drug}
    else:
        return {"message": "return 1 around!"}


""" DELETE """


@drug_router.delete("/drugs/delete/{drug_id}")
def delete_drug(admin_id: int, drug_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()

    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role.value == "admin":
        db_drug = db.query(Drugs).filter(Drugs.id == drug_id).first()

        if not db_drug:
            return {"message": "Drug not found"}

        db.delete(db_drug)
        db.commit()
        return {"message": "deleted", "success": True}
    else:
        return {"message": "return 1 around!"}


""" OTHER """


@drug_router.post("/drugs/amount-update/")
def drug_amount_update(admin_id: int, drug: DrugAmountUpdate, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()

    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role.value == "admin":
        db_drug = db.query(Drugs).filter(Drugs.id == drug.id).first()

        if db_drug is None:
            raise HTTPException(status_code=404, detail="Drug not found")

        db_drug.amount += drug.amount
        db.commit()
        db.refresh(db_drug)
        return {"message": "updated amount", "success": True, "data": db_drug}
    else:
        return {"message": "return 1 around!"}


@drug_router.get("/drugs/low-amount/")
def drug_low_amount(admin_id: int, number: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()

    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.role.value == "admin":
        drugs = db.query(Drugs).filter(Drugs.amount <= number).all()

    return {"message": "updated amount", "success": True, "data": drugs}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Users
from app.schemas import UsersBase

user_router = APIRouter()

""" POST """


@user_router.post("/users/register/")
def register(user: UsersBase, db: Session = Depends(get_db)):  # noqa: B008
    new_user = Users(
        username=user.username,
        password=user.password,
        full_name=user.full_name,
        role=user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


""" GET """


@user_router.get("/users/")
def get_users(db: Session = Depends(get_db)):  # noqa: B008
    users = db.query(Users).all()
    return users


@user_router.get("/users/admins/")
def get_admin_users(db: Session = Depends(get_db)):  # noqa: B008
    db_user = db.query(Users).filter(Users.role == "ADMIN").all()
    return db_user


@user_router.get("/users/cashier/")
def get_cashier_users(db: Session = Depends(get_db)):  # noqa: B008
    db_user = db.query(Users).filter(Users.role == "CASHIER").all()
    return db_user


@user_router.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_user = db.query(Users).filter(Users.id == user_id).first()

    if not db_user:
        return {"message": "User not found"}

    return db_user


""" PUT """


@user_router.put("/users/update/{user_id}")
def update_user(user_id: int, user: UsersBase, db: Session = Depends(get_db)):  # noqa: B008
    db_user = db.query(Users).filter(Users.id == user_id).first()

    if not db_user:
        return {"message": "User not found"}

    db_user.username = user.username
    db_user.password = user.password
    db_user.full_name = user.full_name
    db_user.role = user.role

    db.commit()
    db.refresh(db_user)
    return db_user


""" DELETE """


@user_router.delete("/users/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_user = db.query(Users).filter(Users.id == user_id).first()

    if not db_user:
        return {"message": "User not found"}

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}

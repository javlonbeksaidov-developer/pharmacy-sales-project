from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Users
from app.schemas import UsersBase, UserUpdate

user_router = APIRouter(tags=["User router"])

""" POST """


@user_router.post("/users/register/")
def register(admin_id: int, user: UsersBase, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        new_user = Users(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        return {"message": "return 1 around!"}


""" GET """


@user_router.get("/users/")
def get_users(admin_id: int, start: int = 0, skip: int = 10, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_users = db.query(Users).all()
        users = db_users[start:skip]
        return users
    else:
        return {"message": "return 1 around!"}


@user_router.get("/users/admins/")
def get_admin_users(admin_id: int, start: int = 0, skip: int = 10, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_user = db.query(Users).filter(Users.role == "ADMIN").all()
        admins = db_user[start:skip]
        return admins
    else:
        return {"message": "return 1 around!"}


@user_router.get("/users/cashier/")
def get_cashier_users(admin_id: int, start: int = 0, skip: int = 10, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_user = db.query(Users).filter(Users.role == "CASHIER").all()
        cashiers = db_user[start:skip]
        return cashiers
    else:
        return {"message": "return 1 around!"}


@user_router.get("/users/{user_id}")
def get_user_by_id(admin_id: int, user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_user = db.query(Users).filter(Users.id == user_id).first()
        if not db_user:
            return {"message": "User not found"}
        return db_user
    else:
        return {"message": "return 1 around!"}


""" PUT """


@user_router.put("/users/update/{user_id}")
def update_user(admin_id: int, user_id: int, user: UserUpdate, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_user = db.query(Users).filter(Users.id == user_id).first()

        if not db_user:
            return {"message": "User not found"}

        new_user = user.model_dump(exclude_unset=True)

        for key, value in new_user.items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return {"message": "return 1 around!"}


""" DELETE """


@user_router.delete("/users/delete/{user_id}")
def delete_user(admin_id: int, user_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if admin.role.value == "admin":
        db_user = db.query(Users).filter(Users.id == user_id).first()

        if not db_user:
            return {"message": "User not found"}

        db.delete(db_user)
        db.commit()
        return {"message": "User deleted"}
    else:
        return {"message": "return 1 around!"}

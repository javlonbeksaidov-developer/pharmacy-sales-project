from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Users
from app.schemas import UsersBase

user_router = APIRouter()


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


@user_router.get("/users/")
def get_users(db: Session = Depends(get_db)):  # noqa: B008
    users = db.query(Users).all()
    return users

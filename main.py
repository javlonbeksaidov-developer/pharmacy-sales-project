from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes_check import check_router
from app.routes_check_item import check_item_router
from app.routes_drug import drug_router
from app.routes_user import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(drug_router)
app.include_router(check_router)
app.include_router(check_item_router)

Base.metadata.create_all(engine)


@app.get("/")
def welcome():
    return {"message": "Welcome to DORIXONA project!"}

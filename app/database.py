from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

URL_DB = "sqlite:///./dorixona.db"

engine = create_engine(URL_DB)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Depends

from connectors.sql import SessionLocal
from models.User import User


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(email: str, db: SessionLocal = Depends(get_db)):
    return db.query(User).filter(User.email == email).first()

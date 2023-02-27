from fastapi import Depends
from sqlalchemy.orm import Session

from connectors.sql import SessionLocal
from schemas.User import UserCredentials
from src.models import Crud


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserController:

    def signin(self, user_credentials: UserCredentials, db: Session = Depends(get_db)):
        user = Crud.get_user(db, user_credentials.email)
        return user

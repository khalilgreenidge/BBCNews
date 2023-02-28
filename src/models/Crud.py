from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from connectors.sql import session
from models.User import User


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()


def get_user(email_arg: str):
    db = session
    user = db.execute(select(User).filter_by(email=email_arg)).scalar_one()
    return user

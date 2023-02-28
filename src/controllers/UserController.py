from fastapi import Depends
from sqlalchemy.orm import Session

from connectors.sql import session
from schemas.User import UserCredentials
from src.models import Crud


class UserController:

    def signin(self, user_credentials: UserCredentials):
        user = Crud.get_user(user_credentials.email)
        return user

"""Router (resource) for users."""
from fastapi import APIRouter
from controllers.UserController import UserController
from schemas.User import UserCredentials, User

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"body": "item not found"}})


@router.post("/signin", response_model=User)
def signin(user_login: UserCredentials):
    return UserController().signin(user_login)

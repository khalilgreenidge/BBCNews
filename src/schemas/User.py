from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    email: str


class User(UserBase):
    name: str
    dob: date
    country: str
    gender: str
    cell: str
    last_login: str
    date_created: date

    class Config:
        orm_mode = True


class UserCredentials(UserBase):
    password: str

    class Config:
        orm_mode = True

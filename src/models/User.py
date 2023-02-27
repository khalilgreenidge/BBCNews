from connectors.sql import Base
from sqlalchemy import Column, Integer, String, Date


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    dob = Column(Date)
    country = Column(String)
    gender = Column(String)
    cell = Column(String)
    last_login = Column(String)
    date_created = Column(Date)

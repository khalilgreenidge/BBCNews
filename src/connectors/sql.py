from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from src.config import Config

DATABASE_URL = "mysql+mysqldb://{}:{}@{}/{}".format(
        Config.DB_USER,
        Config.DB_PASS,
        Config.DB_HOST,
        Config.DB_NAME)

engine = create_engine(
    DATABASE_URL, echo=True
)

session = Session(engine)




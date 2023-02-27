import os
from os.path import abspath, join, dirname, pardir
from dotenv import load_dotenv

dotenv_path = abspath(join(dirname(__file__), pardir, '.env'))
load_dotenv(dotenv_path)
environment = os.environ


class Config:
    DB_USER = environment["DB_USER"]
    DB_PASS = environment["DB_PASS"]
    DB_HOST = environment["DB_HOST"]
    DB_PORT = environment["DB_PORT"]
    DB_NAME = environment["DB_NAME"]
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)

session_maker = sessionmaker(autoflush=False, bind=engine)

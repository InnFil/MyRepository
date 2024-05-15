from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from crm.config import database_key

engine = create_engine(database_key)

session_maker = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

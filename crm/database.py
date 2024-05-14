from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

my_database = "postgresql://postgres:1234@127.0.0.1:5432/postgres"

engine = create_engine(my_database)

Session_maker = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

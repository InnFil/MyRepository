from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import mapped_column

from database import Base, engine


class Flat(Base):
    __tablename__ = "flats"

    id = mapped_column(Integer, primary_key=True, unique=True)
    price = mapped_column(Integer)
    description = mapped_column(String)
    square = mapped_column(Integer)
    rooms = mapped_column(Integer)
    number = mapped_column(Integer, unique=True)
    status = mapped_column(String)
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())


Base.metadata.create_all(bind=engine)

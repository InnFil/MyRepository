from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import mapped_column, Mapped

from crm.database import Base


class Flat(Base):
    __tablename__ = "flats"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    photo: Mapped[bytes]
    price: Mapped[int]
    description: Mapped[str]
    square: Mapped[int] = mapped_column(nullable=False)
    rooms: Mapped[int] = mapped_column(nullable=False)
    number: Mapped[int] = mapped_column(unique=True, nullable=False)
    status: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())

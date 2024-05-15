from database import engine, session_maker
from models import Flat
from schema import FlatSchema


def add_flat(new_flat: FlatSchema) -> None:
    with session_maker(autoflush=False, bind=engine) as db:
        flat = Flat(**new_flat.dict())
        db.add(flat)
        db.commit()
        db.refresh(flat)

from pydantic import BaseModel


class FlatSchema(BaseModel):
    price: int
    photo: bytes
    description: str
    square: int
    rooms: int
    number: int
    status: str

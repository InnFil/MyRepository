from pydantic import BaseModel


class FlatSchema(BaseModel):
    price: int
    description: str
    square: int
    rooms: int
    number: int
    status: str

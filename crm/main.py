from fastapi import FastAPI

from schema import FlatSchema
from repository import add_flat


app = FastAPI()


@app.post("/flat/")
def create_flat(new_flat: FlatSchema):
    add_flat(new_flat)
    return {'status': 'ok'}

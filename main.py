import fastapi
from typing import List, Set, Dict, Tuple, Optional
import pydantic
from yushan.data.db import initDatabase
from dataclasses import dataclass

app = fastapi.FastAPI()
db = initDatabase()

class Entity(pydantic.BaseModel) :
    thing:int
    another:str = None
    foo:str = "thing"

@app.get("/")
def read_root():
    return {"hello": "my friends"}

@app.get("/items/{item_id}", response_model=Entity)
def read_item(item_id: int, q: str = None):
    return {"thing":1, "another": "hohoho", "foo": "santa"}

@app.put("/items/")
def put_item(entity: Entity):
    db['entities'].insert(entity.dict())
    print(entity)
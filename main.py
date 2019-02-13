import fastapi
from typing import List, Set, Dict, Tuple, Optional
import pydantic

app = fastapi.FastAPI()

class Entity(pydantic.BaseModel) :
    thing:int
    another:str = None

@app.get("/")
def read_root():
    return {"hello": "my friends"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/")
def put_item(entity: Entity):
    print(entity)
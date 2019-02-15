import dataset
import pydantic

class EntityBase(pydantic.BaseModel):
    name: str
    author: str
    phylum: str
    order: str
    genus: str

class EntityCharacter(EntityBase):
    player: str

class Entity(pydantic.BaseModel):
    name: str
    

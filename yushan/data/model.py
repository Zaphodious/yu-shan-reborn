import dataset
import pydantic

class EntityBase(pydantic.BaseModel):
    name: str
    phylum: str
    order: str
    genus: str

class AttributeChar(EntityBase):
    strength: int = 1
    dexterity: int = 1
    stamina: int = 1
    charisma: int = 1
    manipulation: int = 1
    appearance: int = 1
    perception: int = 1
    intelligence: int = 1
    wits: int = 1

class AbilityChar(EntityBase):
    archery: int = 0
    athletics: int = 0
    awareness: int = 0
    brawl: int = 0
    bureaucracy: int = 0
    dodge: int = 0
    integrity: int = 0
    investigation: int = 0
    larceny: int = 0
    linguistics: int = 0
    lore: int = 0
    medicine: int = 0
    melee: int = 0
    occult: int = 0
    performance: int = 0
    presence: int = 0
    resistance: int = 0
    ride: int = 0
    sail: int = 0
    socialize: int = 0
    stealth: int = 0
    survival: int = 0
    thrown: int = 0
    war: int = 0


class EntityCharacter(AttributeChar, AbilityChar):
    player: str

class Entity(pydantic.BaseModel):
    name: str
    

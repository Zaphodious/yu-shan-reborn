import dataset
from dataclasses import dataclass

def initDatabase():
    db = dataset.connect('sqlite:///db1.sqlite')
    db.create_table('entities')
    db.create_table('relationships')
    return db

@dataclass
class Disk:
    db = initDatabase()
    entities = db['entities']
    relationships = db['relationships']
    

db = dataset.connect('sqlite:///thing')

table = db['jaja']
table.insert({'mything':'hello'})
table
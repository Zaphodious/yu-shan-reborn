import dataset

def initDatabase():
    db = dataset.connect('sqlite:///db1.sqlite')
    db.create_table('entities')


db = dataset.connect('sqlite:///thing')

table = db['jaja']
table.insert({'mything':'hello'})
table
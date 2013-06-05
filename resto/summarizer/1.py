from sqlalchemy import *

engine = create_engine('postgresql://postgres:password@localhost:5432/bursts')
db = engine.connect()

results = db.execute('select * from tw20130203_sb')

for row in results:
    print row

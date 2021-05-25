import sqlalchemy as db


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

films = Table(
    'films', meta,
    Column('id', Integer, primary_key= True),
    Column('name', String),
    Column('director', ForeignKey('director.id')),
    Column('cast', ForeignKey('cast.id')),
    Column('vod', ForeignKey('vod.id'))
)
vod = Table(
    'vod', meta,
    Column('id', Integer, primary_key= True),
    Column('name', String),
    Column('movie_id', Integer)
)
cast = Table(
    'cast', meta,
    Column('id', Integer, primary_key= True),
    Column('name', String),
    Column('SurName', String)
)
director = Table(
    'director', meta,
    Column('id', Integer, primary_key= True),
    Column('name', String),
    Column('surName', String)
)
meta.create_all(engine)
#print("these are columns in our table %s" %(films.columns.keys()))


class Film:
    cast = []
    def __init__(self, name, director, cast, vod):
        self.name = name
        self.director = director
        self.cast = cast
    def AddActor(self):
        actor = input("Wprowadź imię i nazwosko aktora")
        self.cast.append(actor)
    def AddVod(self):
        vod = input("Wprowadź vod")
        self.cast.append(vod)

ins = films.insert()
ins = films.insert().values(name = 'ddfs', director = 'asdas', cast = 'sad aasd asdads', vod = 'Netflix')
conn = engine.connect()
result = conn.execute(ins)


conn.execute(films.insert(), [
   {'name':'Smoleńsk', 'director' : 'guptha', 'cast' : 'adsads', 'vod' : 'Netflix'},
   {'name':'LOTR','director' : 'kumar', 'cast' : 'adsads', 'vod' : 'Netflix'},
   {'name':'Harry Potter','director' : 'varma', 'cast' : 'adsads', 'vod' : 'Netflix'},
   {'name':'Tomb Raider','director' : 'varma', 'cast' : 'adsads', 'vod' : 'Netflix'},
   {'name':'Wszyscy moi przyjaciele nie żyją','director' : 'Jan Belcla', 'cast' : 'Julia Wieniewa', 'vod' : 'Netflix'},
])

conn = engine.connect()
stmt = films.delete().where(films.c.name == 'Smoleńsk')
conn.execute(stmt)
s = films.select()
conn.execute(s).fetchall()

conn = engine.connect()
stmt = films.update().where(films.c.name == 'LOTR').values(name = 'Tomb Raider')
conn.execute(stmt)
s = films.select()
conn.execute(s).fetchall

s = films.select()
result = conn.execute(s)
for row in result:
   print (row)

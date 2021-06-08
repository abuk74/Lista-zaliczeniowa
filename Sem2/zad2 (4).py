from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///collage.db', echo = True)
meta = MetaData()

movies = Table(
    'movies', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('director', String),
    Column('cast', String),
    Column('vod', String)
)

meta.create_all(engine)

print("these are columns in our table %s" %(movies.columns.keys()))

class Movie:

    cast = []

    def __init__(self, title, director, cast):
        self.title = title
        self.director = director
        self.cast = cast

    def AddActor(self):
        actor = input("")
        self.cast.append(actor)

    def AddVod(self):
        vod = input("")
        self.cast.append(vod)

ins = movies.insert()
ins = movies.insert().values(title = 'TheGodfather', director = 'idk', cast = 'idk', vod = 'mby')
conn = engine.connect()
result = conn.execute(ins)

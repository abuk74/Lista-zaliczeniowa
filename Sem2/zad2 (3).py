import os
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if os.path.exists('match.db'):
    os.remove('match.db')
base_op = create_engine('sqlite:///match.db')

base = declarative_base()

class Team(base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teammate_id = Column(Integer, ForeignKey("teammates.id"))

class Teammates(base):
    __tablename__ = "teammates"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    team = relationship('Team', 'teammates')

class Matches(base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    team1 = relationship("Team", "matches")
    team2 = relationship("Team", "matches")
    score = Column(String, nullable=False)

base.metadata.create_all(base_op)
BDSession = sessionmaker(bind=base_op)
session = BDSession()
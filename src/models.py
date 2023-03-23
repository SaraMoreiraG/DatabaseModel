import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    birth_year = Column(Integer)
    gender = Column(String(30))
    homeworld = Column(String(250))
    url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(30))
    population  = Column(Integer)
    climate = Column(String(30))
    terraint = Column(String(30))
    url = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character_name = Column(Integer, ForeignKey('character.name'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet_name = Column(Integer, ForeignKey('planet.name'))
    planet = relationship(Planet)

    favorite_name = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

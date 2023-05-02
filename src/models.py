import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=False, nullable=False)

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer(), ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    comment = Column(String(250), unique=True, nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer(), ForeignKey('post.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'), nullable=False)
    tittle = Column(String(40), unique=True, nullable=False)
    image = Column(Integer(), unique=False, nullable=False)
    description = Column(String(120), unique=True, nullable=False)
    comments = relationship(Comments)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    full_name = Column(String(80), unique=False, nullable=True)
    age = Column(Integer(), unique=False, nullable=True)
    description = Column(String(120), unique=False, nullable=True)
    country = relationship(Country)
    posts = relationship(Post)
    favorites = relationship(Favorites)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
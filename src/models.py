import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Boolean, DateTime, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Web user data
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    name = Column(String(50), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(15), nullable=False)
    is_active = Column(Boolean)
    
# User posts
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    title = Column(String(250))
    comment = Column(String(140))
    image_url = Column(String(250))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

# User likes
class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship(User)
    post = relationship(Post)

## Draw from SQLAlchemy base
render_er(Base, "diagram.png")

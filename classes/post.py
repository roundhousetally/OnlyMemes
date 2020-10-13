#!/usr/bin/python3
""" Posts class """
from datetime import datetime
import sqlalchemy
from classes import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    """ The post """
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String(120), nullable=True)
    media = Column(String(50), nullable=True)
    likes = Column(Integer, nullable=False, default=0)
    shares = Column(Integer, nullable=False, default=0)
    datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)

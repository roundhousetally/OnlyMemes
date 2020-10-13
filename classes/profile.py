#!/usr/bin/python3
""" Contains the Profile class """

from classes import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Profile(Base):
    """ Definition of a profile on the website. """
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    description = Column(String(240), nullable=True)
    api = Column(String(100), nullable=False)
    pfp = Column(String(25), nullable=True)
    posts = relationship("Posts", backref="profile")

    def __init__(self, **kwargs):
        """ Initilizes profile instance. """
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)

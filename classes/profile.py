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

    def save(self):
        """ Adds the instance to the database session. """
        models.storage.new(self)

    def delete(self):
        """ Removes the instance from the database session. """
        models.storage.delete(self)

    def __str__(self):
        """ Returns a string representation of the instance. """
        return "{}[{}] - {} ({} posts)".format(name, id, description[:15] + ('...' if len(description) > 15 else ''), len(posts))

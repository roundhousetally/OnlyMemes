#!/usr/bin/python3
""" Contains the Profile class """
from classes.base import Base, Parent
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Profile(Parent, Base):
    """ Definition of a profile on the website. """
    __tablename__ = 'profiles'
    name = Column(String(20), unique=True, nullable=False)
    description = Column(String(240), nullable=True)
    api = Column(String(100), nullable=False)
    pfp = Column(String(25), nullable=True)
    posts = relationship("Post", backref="profile")

    def __str__(self):
        """ Returns a string representation of the instance. """
        return "{}[{}] - {} ({} posts)".format(self.name, self.id, self.description[:15] + ('...' if len(self.description) > 15 else ''), len(self.posts))

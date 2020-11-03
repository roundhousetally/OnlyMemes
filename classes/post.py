#!/usr/bin/python3
""" Contains the Posts class which represents rows in the posts table. """
from datetime import datetime
from classes.base import Parent, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Post(Parent, Base):
    """ Represents rows in the posts table of the database. """
    __tablename__ = 'posts'
    text = Column(String(240), nullable=True)
    media = Column(String(100), nullable=True)
    likes = Column(Integer, nullable=False, default=0)
    shares = Column(Integer, nullable=False, default=0)
    datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    profile_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)

    def __str__(self):
        """ Returns a string representation of the instance. """
        return "[{}]Owner: {} - hasText={} hasMedia={} \
                ({} likes, {} shares)".format(self.id, self.profile.name,
                                              self.text is not None,
                                              self.media is not None,
                                              self.likes, self.shares)

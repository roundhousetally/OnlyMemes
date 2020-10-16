#!/usr/bin/python3
""" Posts class """
from datetime import datetime
from classes.base import Parent, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Post(Parent, Base):
    """ The post """
    __tablename__ = 'posts'
    text = Column(String(120), nullable=True)
    media = Column(String(50), nullable=True)
    likes = Column(Integer, nullable=False, default=0)
    shares = Column(Integer, nullable=False, default=0)
    datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    profile_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)

    def __str__(self):
        """ Returns a string representation of the instance. """
        return "[{}]Owner: {} - hasText={} hasMedia={} ({} likes, {} shares)".format(self.id, self.profile.name, self.text is not None, self.media is not None, self.likes, self.shares)

#!/usr/bin/python3
""" Contains the Parent class. """

import classes
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parent:
    """ Parent class for Profile and Post. """
    id = Column(Integer, primary_key=True)

    def save(self):
        """ Adds the instance to the database session. """
        classes.storage.new(self)

    def delete(self):
        """ Removes the instance from the database session. """
        classes.storage.delete(self)

#!/usr/bin/python3
""" Contains the Parent class and base for all db objects. """

import classes
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# The base that all db objects will inherit from
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

    def to_dict(self):
        """ Returns a dictionary representation of the instance. """
        res = self.__dict__.copy()

        # Translate datetime into string
        if "datetime" in res:
            res["datetime"] = res["datetime"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        # Delete unneeded attributes
        if "posts" in res:
            del res["posts"]
        if "profile" in res:
            del res["profile"]
        if "_sa_instance_state" in res:
            del res["_sa_instance_state"]

        return res

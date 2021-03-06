#!/usr/bin/python3
""" Contains the Storage class which handles database interaction. """

from classes.base import Base
from classes.profile import Profile
from classes.post import Post
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker


class Storage:
    """ Handles the MariaDB database interactions. """
    __engine = None
    __session = None

    def __init__(self):
        """ Sets up the database. """
        self.__engine = create_engine('mysql+mysqldb://onlymemes:SaLT@localhost/onlymemes')

    def getProfile(self, id=None, name=None):
        """ Returns one or more Profile objects from the database. """
        data = self.__session.query(Profile)  # Grabs all profiles from database

        # Checks what profiles we are trying to get
        if id is not None:
            # Gets all profiles matching id
            data = data.filter_by(id=id).all()
        elif name is not None:
            # Gets all profiles matching name
            data = data.filter_by(name=name).all()
        else:
            # Gets all profiles
            data = data.all()

        return data

    def getPost(self, post_id=None, profile_id=None):
        """ Returns one or more Post objects from the database. """
        data = self.__session.query(Post)  # Grabs all posts from database

        # Checks what posts we are trying to get
        if post_id is not None:
            # Gets all posts by id
            data = data.filter_by(id=post_id).order_by(-Post.datetime).all()
        elif profile_id is not None:
            # Gets all posts by profile_id
            data = data.filter_by(profile_id=profile_id).order_by(-Post.datetime).all()
        else:
            # Gets all posts
            data = data.order_by(-Post.datetime).all()

        return data

    def new(self, obj):
        """ Adds an object to the database. """
        self.__session.add(obj)
        return obj

    def save(self):
        """ Commits all changes to the database. """
        self.__session.commit()

    def delete(self, obj):
        """ Deletes an object from the database. """
        self.__session.delete(obj)

    def load(self):
        """ Starts the database session. """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ Closes the current database session. """
        self.__session.remove()

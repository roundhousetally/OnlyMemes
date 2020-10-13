#!/usr/bin/python3
""" Sets up relationship of posts to profiles """
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Profile_to_Posts():
    """ Sets up the relationsip """
    

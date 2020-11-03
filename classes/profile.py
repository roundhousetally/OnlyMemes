#!/usr/bin/python3
""" Contains the Profile class which represents rows in the profiles table. """
from classes.base import Base, Parent
from classes.post import Post
import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import requests


class Profile(Parent, Base):
    """ Represents rows in the profiles table of the database. """
    __tablename__ = 'profiles'
    name = Column(String(20), unique=True, nullable=False)
    description = Column(String(240), nullable=True)
    api = Column(String(100), nullable=False)
    pfp = Column(String(50), nullable=True)
    posts = relationship("Post", backref="profile")

    def post(self):
        """ Generates a new post on the profile. """
        p = Post()  # Creates the post object

        # Pulls from the assigned API
        stuff = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(self.api, headers=stuff).json()

        # Checks the structure of and pulls information from the json
        if isinstance(r, list):
            r = r[0]
        if 'punchline' in r:
            p.text = r.get('setup') + '\n' + r.get('punchline')
        elif 'slip' in r:
            p.text = r['slip']['advice']
        elif 'url' in r:
            p.media = r['url']
        elif 'data' in r:
            num = random.randint(0, 100)
            link = r.get('data').get('children')[num].get('data').get('url')
            if '.jpg' in link or '.png' in link:
                p.media = link

        # If API pull fails, abort creation, otherwise save the new post
        if p.media is None and p.text is None:
            del p
        else:
            p.profile_id = self.id
            p.save()

    def __str__(self):
        """ Returns a string representation of the instance. """
        return "{}[{}] - {} ({} posts)".format(self.name, self.id,
                                               self.description[:15] + ('...' if len(self.description) > 15 else ''),
                                               len(self.posts))

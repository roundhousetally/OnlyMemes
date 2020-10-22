#!/usr/bin/python3
""" Contains the Profile class """
from classes.base import Base, Parent
from classes.post import Post
import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import requests

class Profile(Parent, Base):
    """ Definition of a profile on the website. """
    __tablename__ = 'profiles'
    name = Column(String(20), unique=True, nullable=False)
    description = Column(String(240), nullable=True)
    api = Column(String(100), nullable=False)
    pfp = Column(String(50), nullable=True)
    posts = relationship("Post", backref="profile")

    def post(self):
        """ Tells the profile to generate a new post. """
        p = Post()
        stuff = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(self.api, headers=stuff).json()
        if isinstance(r, list):
            r = r[0]
        if 'value' in r:
            p.text = r['value']
        elif 'slip' in r:
            p.text = r['slip']['advice']
        elif 'url' in r:
            p.media = r['url']
        elif 'data' in r:
            num = random.randint(0, 100)
            link = r.get('data').get('children')[num].get('data').get('url')
            if '.jpg' in link or '.png' in link:
                p.media = link
        if p.media is None and p.text is None:
            del p
        else:
            p.profile_id = self.id
            p.save()

    def __str__(self):
        """ Returns a string representation of the instance. """
        return "{}[{}] - {} ({} posts)".format(self.name, self.id, self.description[:15] + ('...' if len(self.description) > 15 else ''), len(self.posts))

#!/usr/bin/python3
""" Testing the API stuff IDK I'm not paid enough for this """
from api import app_views
from flask import abort, jsonify
from flask.globals import requests


settings = {
    'strict_slashes': False,
    'methods': ['GET']
}

@app_views.route('/posts' **settings)
def posts(profile_id=None):
    if profile_id = None:
        print("Profile ID expected")
    

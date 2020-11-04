#!/usr/bin/python3
""" This is where all the API routes are defined """
from omAPI.views import app_views
from flask import abort, jsonify, request
from classes import storage
from classes.post import Post
from classes.profile import Profile
import json


# Information for API settings
settings = {
    'strict_slashes': False,
    'methods': ['GET', 'POST']
}


@app_views.route('/posts/<int:profile_id>/<int:page>', **settings)
def posts(profile_id=None, page=0):
    """ Gets a list of posts based on Profile ID and page  """
    if request.method == 'GET':
        if profile_id is None:
            return ("Profile ID expected")
        info = storage.getPost(profile_id=profile_id)
        # This deals with the pagination of the posts
        if len(info) >= page*25+25:
            info = info[page*25:25*page+25]
        else:
            ending = {'ending': 'right here m8'}
            if len(info) >= page*25:
                info = info[page*25:]
                info.append(ending)
            else:
                return json.dumps([ending])
        for i in range(len(info)):
            if type(info[i]) is not dict:
                info[i] = info[i].to_dict()
        return json.dumps(info)
    else:
        # This is for the case in which the API needs to post a post
        new_post = storage.new(Post())
        if not request.get_json():
            abort(400, description="Not a JSON")
        data = request.get_json()
        for key, val in data.items():
            setattr(new_post, key, val)
        new_post.save()
        storage.save()
        return json.dumps(new_post.to_dict())

@app_views.route('/profiles/<name>', **settings)
def profile(name=None):
    """ Get a Profile based on its name  """
    if request.method == 'GET':
        info = storage.getProfile()
        if name is None:
            for i in range(len(info)):
                info[i] = info[i].to_dict()
            return json.dumps(info)
        return json.dumps(storage.getProfile(name=name)[0].to_dict())

@app_views.route('/profiles', **settings)
def profiles():
    """ Get a list of all profiles  """
    if request.method == 'GET':
        info = storage.getProfile()
        for i in range(len(info)):
            info[i] = info[i].to_dict()
        return json.dumps(info)

#!/usr/bin/python3
""" Testing the API stuff IDK I'm not paid enough for this """
from omAPI.views import app_views
from flask import abort, jsonify, request
from classes import storage
from classes.post import Post
from classes.profile import Profile
import json


settings = {
    'strict_slashes': False,
    'methods': ['GET', 'POST']
}

@app_views.route('/posts/<int:profile_id>', **settings)
def posts(profile_id=None):
    if request.method == 'GET':
        if profile_id is None:
            return ("Profile ID expected")
        info = storage.getPost(profile_id=profile_id)
        for i in range(len(info)):
            info[i] = info[i].to_dict()
        return json.dumps(info)
    else:
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
    if request.method == 'GET':
        info = storage.getProfile()
        if name is None:
            for i in range(len(info)):
                info[i] = info[i].to_dict()
            return json.dumps(info)
        return json.dumps(storage.getProfile(name=name)[0].to_dict())

@app_views.route('/profiles', **settings)
def profiles():
    if request.method == 'GET':
        info = storage.getProfile()
        for i in range(len(info)):
            info[i] = info[i].to_dict()
        return json.dumps(info)

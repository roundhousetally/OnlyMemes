#!/usr/bin/python3
"""
Creates the blueprint that is used in the API
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api')

from omAPI.views.test_api import posts

#!/usr/bin/python3
"""
Start the Flask
"""
from classes import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(404)
def not_found(e):
    """ 404 error handler. """
    return render_template('404page.html')

@app.route('/<profile_name>', strict_slashes=False)
def profile(profile_name=None):
    """ Generates profile page. """
    for profile in storage.getProfiles():
        if profile_name == profile.name:
            return render_template('prof1.html')
    abort(404)

if __name__ == "__main__":
    """ Main here """
    app.run(host='0.0.0.0', port='5001')

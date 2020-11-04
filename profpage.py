#!/usr/bin/python3
""" Contains the Flask app and starts it when ran. """
from classes import storage
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Closes storage. """
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """ 404 error handler. """
    return render_template('404page.html')


@app.route('/<profile_name>', strict_slashes=False)
def profile(profile_name=None):
    """ Generates and serves a profile page. """
    # Loops through and checks if the requested profile exists.
    for profile in storage.getProfile():
        if profile_name.replace('-', ' ') == profile.name:
            return render_template('prof1.html')
    abort(404)

# Runs only if this file is called as main.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')

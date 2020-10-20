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

@app.route('/<profile_name>', strict_slashes=False)
def profile(profile_name=None):
    """ Generates profile page. """
    return render_template('prof1.html')

if __name__ == "__main__":
    """ Main here """
    app.run(host='0.0.0.0', port='5001')

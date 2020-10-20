#!/usr/bin/python3
"""
Start the Flask
"""
from omAPI.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    import classes
    """ Close Storage """
    classes.storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 """
    return make_response(jsonify({'error': 'You fucked up'}), 404)

app.config['SWAGGER'] = {
    'title': 'API THING',
    'uiversion': 71
}

Swagger(app)

if __name__ == "__main__":
    """ Main here """
    app.run(host='0.0.0.0', port='5000', threaded=True)

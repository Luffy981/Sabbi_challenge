#!/usr/bin/env python3
""" Developing Flask application """
# import pdb; pdb.set_trace()
from os import environ
from api.v1.views import app_views
from models import storage
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close db storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
        404:
            description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
        'title': 'Sabbi survey Restful API',
        'uiversion': 1
        }

Swagger(app)


if __name__ == "__main__":
    """ Start application """
    host = environ.get('SABBI_API_HOST')
    port = environ.get('SABBI_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '3000'

    app.run(host=host, port=port, threaded=True, debug=True)

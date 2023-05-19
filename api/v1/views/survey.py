#!/usr/bin/env python3

""" Objects that handle all default Restful API actions for survey """

from models.survey import Survey
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from models import storage

@app_views.route('/users/<user_id>/survey', methods=['GET'], strict_slashes=False)
def get_user_survey(user_id):
    """
    Retrieves an user survey result
    """
    surveys = storage.all(Survey)
    for value in surveys.values():
        if (value.id_user) == user_id:
            return make_response(jsonify(value.to_dict()))
    return abort(404)

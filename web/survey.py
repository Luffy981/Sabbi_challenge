#!/usr/bin/env python3
""" Show survey to user """

from models import storage, questions, answers
from os import environ
from flask import Flask, render_template, jsonify, request


# Application instance
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/survey', methods=['GET'], strict_slashes=False)
def get_survey():
    """ Mixing question + answer """
    question_answer = {questions[key]: answers[key] for key in questions}
    return render_template('survey.html', question_answer=question_answer)

@app.route('/survey/submit', methods=['POST'], strict_slashes=False)
def submit_survey():
    """ Survey to user """
    answers = request.form.to_dict()
    # print(answers)

    # return jsonify({'message': 'Answers sent successfully'})
    return jsonify(answers)

if __name__ == "__main__":
    """ Main function """
    app.run(host='0.0.0.0', port=5000, debug=True)

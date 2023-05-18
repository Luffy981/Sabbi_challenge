#!/usr/bin/env python3
""" Show survey to user """

from models import storage, questions, answers
from os import environ
from flask import Flask, render_template, jsonify, request, redirect, url_for


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
    answers = request.get_json()
    percent = [0.1, 0.1, 0.15, 0.25, 0.4]
    i = 0
    total = 0
    # print("Soy respuest", answers)
    for question in questions.values():
        print(answers[question])
        total += int(answers[question]) * percent[i]
        i += 1
    total = round(total, 2)
    print("TOTAL: ", total)
    flag = 0
    if total < 2:
        message = "Eres perfil conservador 🤓"
    elif total >= 2 and total < 3.5:
        message = "Eres perfil moderado 🙂 "
    else:
        message = "Eres perfil arriesgado 😎"
        flag = 1

    if flag == 1:
        message2 = "Te recomendamos INVERTIR en el Fondo de Fondos Sabbi Hedge Fund FMIV 🚀"
    else:
        message2 = "Te recomendamo NO INVERTIR en el Fondo de Fondos Sabbi Hedge Fund FMIV"

    # return jsonify({'message': 'Answers sent successfully'})
    return redirect(url_for('show_results',
                            message=message,
                            recomendation=message2))

@app.route('/survey/results', methods=['GET'], strict_slashes=False)
def show_results():
    """ Show results page """
    message = request.args.get('message')
    recomendation = request.args.get('recommendation')
    return render_template('results.html',
                           message=message,
                           recomendation=recomendation)
if __name__ == "__main__":
    """ Main function """
    app.run(host='0.0.0.0', port=5000, debug=True)

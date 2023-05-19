#!/usr/bin/env python3
""" Show survey to user """
from models.survey import Survey
from models import storage, questions, answers
from os import environ
from flask import Flask, render_template, jsonify, request, redirect, url_for, make_response
# Application instance
app = Flask(__name__)



@app.route('/survey', methods=['GET'], strict_slashes=False)
def get_survey():
    """ Mixing question + answer """
    question_answer = {questions[key]: answers[key] for key in questions}
    return render_template('survey.html', question_answer=question_answer)

@app.route('/survey/submit', methods=['POST'], strict_slashes=False)
def submit_survey():
    """ Survey to user """
    response = request.get_json()
    percent = [0.1, 0.1, 0.15, 0.25, 0.4]
    i = 0
    total = 0
    # print("Soy respuest", answers)
    for question in questions.values():
        print(response[question])
        total += int(response[question]) * percent[i]
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
        recommend = "Te recomendamos INVERTIR en el Fondo de Fondos Sabbi Hedge Fund FMIV 🚀"
    else:
        recommend = "Te recomendamo NO INVERTIR en el Fondo de Fondos Sabbi Hedge Fund FMIV"
    data = {
            'status_s': True,
            'total_calculated': total,
            'result': message,
            'id_user': 1,
            'recomendation': recommend
            }
    instance = Survey(**data)
    instance.save()

    return jsonify({'message': 'Answers sent successfully'})

@app.route('/survey/results', methods=['GET'], strict_slashes=False)
def show_results():
    """ Show results page """
    user_id = 1
    all_cls = storage.all('Survey')
    for value in all_cls.values():
        if (value.id_user == user_id):
            user_found = value

    return render_template('results.html',
                           message=user_found.result,
                           recommendation=user_found.recomendation)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()
    

if __name__ == "__main__":
    """ Main function """
    app.run(host='0.0.0.0', port=4000, debug=True)

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekret_key'

# param = input()
listing = ["Инженер-технолог",
           "Инженер",
           "Строитель",
           "Пилот",
           "Экзобиолог",
           "Физик-ядерщик",
           "Врач",
           "Метеоролог",
           "Инженер жизнеобеспечения",
           "Киберинженер"]

'''@app.route('/')
@app.route(f"/list_prof")
def index():
    return render_template('stations.html', title='Заготовка', par=param, listing=listing,
                           ty=param)'''


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('answer.html', styles=url_for('static', filename='css/styles.css'), d={
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': "Высшее",
        'profession': "Профессор секретного университета",
        'sex': 'male',
        'motivation': "Нам мало места на Земле",
        'ready': True})


app.run(port=8080, host='127.0.0.1')

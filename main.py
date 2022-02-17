from PIL import Image
from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def slash():
    return f"<h3>Миссия Колонизация Марса</h3>"


@app.route('/index')
def index():
    return f"<h3>И на Марсе будут яблони цвести!</h3>"


@app.route('/promotion')
def promotion():
    return f"Человечество вырастает из детства. <br> Человечеству мала одна планета. <br> " \
           f"Мы сделаем обитаемыми безжизненные пока планеты. <br> И начнем с Марса! <br> Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <head><title>Привет, Марс!</title></head>
                <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='img/marsimage.jpeg')}" alt="Здесь должон был быти Марс,
                но он улетел по какой-то ошибке">
                <p>Вот такая она, красная планета</p>
                </body>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <head><title>Колонизация</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                    </head>
                    <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/marsimage.jpeg')}" alt="Здесь должон был быти Марс,
                    но он улетел по какой-то ошибке">
                    <div class="alert alert-primary" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-info" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Присоединяйся!
                    </div>
                    </body>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html>
                        <head><title>Отбор астрономов</title>
                        <link rel="stylesheet" href="{url_for('static', filename='css/form-styles.css')}"></link>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                        </head>
                        <body>
                            <h1>Отбор астрономов</h1>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                <input type="text" class="form-control" id="surname" placeholder="Введите имя" name="name">
                                <input type="email" class="form-control" placeholder="Введите адрес почты" id="email" name="email">
                                <label for="education">Какое у вас образование?</label>
                                <div class="form-group">
                                <select id="education">
                                    <option>Начальное</option>
                                    <option>Среднее</option>
                                    <option>Высшее</option>
                                </select>
                                </div>
                                <label for="job">Какая у вас профессия?</label>
                                <div class="job">
                                    <input id="engineer-discover" type="radio" name="job" value="engineer-discover">
                                    <label for="engineer-discover">Инженер-исследователь</label>
                                </div>
                                <div class="job">
                                    <input id="engineer-builder" type="radio" name="job" value="engineer-builder">
                                    <label for="engineer-builder">Инженер-строитель</label>
                                </div>
                                <div class="job">
                                    <input id="pilot" type="radio" name="job" value="pilot">
                                    <label for="pilot">Пилот</label>
                                </div>
                                <div class="job">
                                    <input id="meteor" type="radio" name="job" value="meteor">
                                    <label for="meteor">Метеоролог</label>
                                </div>
                                <div class="job">
                                    <input id="safety-engineer" type="radio" name="job" value="safety-engineer">
                                    <label for="safety-engineer">Инженер по жизнеобеспечению</label>
                                </div>
                                <div class="job">
                                    <input id="radio-engineer" type="radio" name="job" value="radio-engineer">
                                    <label for="radio-engineer">Инженер по радиационной защите</label>
                                </div>
                                <div class="job">
                                    <input id="doctor" type="radio" name="job" value="doctor">
                                    <label for="doctor">Врач</label>
                                </div>
                                <div class="job">
                                    <input id="exobiolog" type="radio" name="job" value="exobiolog">
                                    <label for="exobiolog">Экзобиолог</label>
                                </div>
                                <label for="sex-group">Пол</label>
                                <div class="sex-group">
                                <div class="sex">
                                    <input class="gender" id="male" name="sex" value="male" type="radio" checked>
                                    <label for="male">Мужской</label>
                                </div>
                                <div class="sex">
                                    <input class="gender" value="female" name="sex" id="female" type="radio">
                                    <label for="female">Женский</label>
                                </div>
                                </div>
                                <div class="motivation-group">
                                    <label for="motivation">Ваша мотивация</label>
                                    <textarea id="motivation" name="motivation" class="motivation" rows="5"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Ваша фотография</label>
                                    <input type="file" id="photo" name="file">
                                </div>
                                <div>
                                    <input type="checkbox" id="accept-rules">
                                    <label for="accept-rules">Готов остаться на Марсе</label>
                                </div>
                                <button type="submit" class="btn-primary">Отправить заявку</button>
                            </form>
                        </body>
                    </html>'''
    elif request.method == 'POST':
        for i in request.form:
            print(request.form[i])
        return f"Форма была отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

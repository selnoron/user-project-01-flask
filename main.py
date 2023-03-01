# Flask
from flask import (
    Flask,
    Request,
    request,
    redirect,
    Response,
    render_template
)
from flask.app import Flask as FlaskApp

# Local
from models.user import *


app: FlaskApp = Flask(__name__)
users_data: list[User] = []
log: str = ''

@app.route('/')
def main_page():
    return render_template(
        'index.html'
    )

@app.route('/auth', methods=['GET', 'POST'])
def auth_page():
    if request.method == 'POST':
        log = request.form.get('login')
        pas: str = request.form.get('password')
        for user in users_data:
            if user.login == log and user.password == pas:
                return render_template(
                    'choice.html'
                )
            
    return render_template(
        'auth.html'
    )

@app.route('/reg', methods=['GET', 'POST'])
def reg_page():
    if request.method == 'POST':
        user = User(
            login=request.form.get('login'),
            password=request.form.get('password'),
            email=request.form.get('email'),
            name=request.form.get('name'),
            surname=request.form.get('surname'),
            age=request.form.get('age')
        )
        users_data.append(user)
        return redirect('/auth')
    
    return render_template(
        'red.html'
    )

@app.route('/users', methods=['GET', 'POST'])
def users_page():
    return render_template(
        'all_users.html',
        data=users_data
    )

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        for user in users_data:
            if user.login == log:
                user.admin = User.administration(user)
    return render_template(
        'admin.html'
    )

if __name__ == '__main__':

    app.run(
        host='localhost',
        port=8080,
        debug=True
    )
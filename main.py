from flask import Flask, render_template, redirect, url_for, request
from config import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main-templates/d-dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/audits')
def audits():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/user-login', methods = ['POST'])
def login():
    login_details = []
    for key, values in request.form.items():
        login_details.append(values)
    db = database.Database()
    if db.login(login_details=login_details) == 'Login Successful':
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('register'))

@app.route('/user-register', methods=['POST'])
def newuser():
    register_users = []
    for key, values in request.form.items():
        register_users.append(values)
    db = database.Database()
    if db.register_users(user_details= register_users) == 'User Registered':
        return redirect(url_for('user'))
    else:
        return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True)
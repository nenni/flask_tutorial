from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/add_user')
def add_user():
    users = models.User.query.all()
    oneuser = models.User.query.filter_by(name="test2").first()
    return render_template("add_user.html", users=users, user2=oneuser)


@app.route('/profile/<user_name>')
def profile(user_name):
    user = models.User.query.filter_by(name=user_name).first()
    return render_template("profile.html", user=user)


@app.route('/post_user', methods=['POST'])
def post_user():
    user = models.User(name=request.form['name'], email=request.form['email'])
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('add_user'))


if __name__ == '__main__':
    app.run(debug=True)


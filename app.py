from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


import models

# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/')
def index():
    return "Hello Flask"


# # Create a user to test with
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='matt@nobien.net', password='password')
#     db.session.commit()


# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/add_user')
def add_user():
    return render_template("add_user.html")


# @app.route('/profile/<user_name>')
# def profile(user_name):
#     user = models.User.query.filter_by(name=user_name).first()
#     return render_template("profile.html", user=user)


@app.route('/post_user', methods=['POST'])
def post_user():
    user = models.User(name=request.form['name'], email=request.form['email'])
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('add_user'))


if __name__ == '__main__':
    app.run(debug=True)


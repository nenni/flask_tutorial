from app import app, db, user_datastore
from flask import render_template, request, url_for, redirect
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from .models import User, Role, roles_users


# @app.route('/')
# def index():
#     return "Hello Flask"


# Create a user to test with
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


@app.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()
    return render_template("profile.html", user=user, title="Profile |")


# @app.route('/add_user')
# def add_user():
#     return render_template("add_user.html")
#
#
# @app.route('/post_user', methods=['POST'])
# def post_user():
#     user = User(name=request.form['name'], email=request.form['email'])
#     db.session.add(user)
#     db.session.commit()
#
#     return redirect(url_for('add_user'))


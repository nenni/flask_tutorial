from app import db
from flask.ext.security import UserMixin, RoleMixin
from datetime import datetime


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


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), unique=True)
    answer = db.Column(db.String(255))
    created_date = db.Column(db.DateTime)

    def __init__(self, question, answer, created_date=None):
        self.question = question
        self.answer = answer
        if created_date is None:
            created_date = datetime.utcnow()
        self.created_date = created_date

    def __repr__(self):
        return """<Question: {}, Answer: {}>""".format(self.question)

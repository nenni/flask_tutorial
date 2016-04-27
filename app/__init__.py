from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from .models import User, Role, roles_users, Questions

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


from app import views, models


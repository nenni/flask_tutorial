import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask security module
SECRET_KEY = 'super-secret'
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'dasdasdasdjkkdsjkasjdkqdwqeiqoweadsa819238192834$!$!$!$DADAD!#!$**((('
SECURITY_SEND_REGISTER_EMAIL = False

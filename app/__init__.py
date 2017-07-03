import os
from flask import Flask
from flask.ext.login import LoginManager
from flask_basicauth import BasicAuth
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

basic_auth = BasicAuth(app)


from app import views, models

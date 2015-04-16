import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask.ext.bcrypt import Bcrypt

app=Flask(__name__)

app.config.from_object('config')
CsrfProtect(app)
bcrypt=Bcrypt(app)
db=SQLAlchemy(app)

from iInvest import views, models

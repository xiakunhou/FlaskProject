import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

app=Flask(__name__)

app.config.from_object('config')
CsrfProtect(app)
db=SQLAlchemy(app)

from iInvest import views, models

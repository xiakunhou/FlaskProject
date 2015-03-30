import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)

from appA import views, models

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask.ext.bcrypt import Bcrypt
#import flask_admin as admin

app=Flask(__name__,template_folder='templates')


app.config.from_object('config')
csrf=CsrfProtect(app)
bcrypt=Bcrypt(app)
db=SQLAlchemy(app)

from iInvest import models, trustProductView, articleView, assetManagementView,login

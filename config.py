import os

CSRF_ENABLED=True
SECRET_KEY='you-will-nerver-guess'

basedir=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='mysql+pymysql://admin:admin@192.168.1.105/investplatform'


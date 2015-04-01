import os

CSRF_ENABLED=True
SECRET_KEY='you-will-nerver-guess'

basedir=os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
                               '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

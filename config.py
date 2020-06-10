import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'You-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.environ.get(basedir, 'sqlite:///'+os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
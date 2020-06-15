import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'You-will-never-guess')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(basedir, 'sqlite:///'+os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', False)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'yooongchun@foxmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'ivkiwwrlfbhvdecb')
    ADMINS = ['yooongchun@foxmail.com']

    POSTS_PER_PAGE = 3

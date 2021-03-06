import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['yooongchun@foxmail.com']

    POSTS_PER_PAGE = 3

    LANGUAGES = ['en', 'zh']

    BAIDU_TRANS_APP_ID = os.environ.get('BAIDU_TRANS_APP_ID')
    BAIDU_TRANS_SECRET_KEY = os.environ.get('BAIDU_TRANS_SECRET_KEY')

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

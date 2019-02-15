import os
basedir = os.path.abspath(os.path.dirname(__file__))

LOCAL_DB_URL = "postgresql:///excedo_db"

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aaaaa'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_DB_URL)

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = LOCAL_DB_URL

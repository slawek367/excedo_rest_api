import os

LOCAL_DB_URL = "postgresql:///excedo_db"

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'aaaaa'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_DB_URL)
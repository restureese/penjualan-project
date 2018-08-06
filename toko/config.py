import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'You Will Never Learn'
    # MYSQL_HOST = 
    # MYSQL_USER = 
    # MYSQL_PASSWORD = 
    # MYSQL_DB = 
    SQLALCHEMY_DATABASE_URI = 'mysql://restureese:@localhost/meubel'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
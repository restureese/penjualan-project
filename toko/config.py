import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'You Will Never Learn'
    # MYSQL_HOST = 
    # MYSQL_USER = 
    # MYSQL_PASSWORD = 
    # MYSQL_DB = 
    SQLALCHEMY_DATABASE_URI = 'mysql://restureese:@localhost/toko'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
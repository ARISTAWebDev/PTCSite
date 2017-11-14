""" All configuration values for the app """

import os

class HardCoded(object):
    """ Constants to be used throughout the application

    All hard coded settings/data that are not actual/official configuration options for Flask, Celery, or their extensions goes here.
    """

    basedir = os.path.abspath(os.path.dirname(__file__))
    
class CeleryConfig(HardCoded):
    """ Celery Configuration """
    
    # TODO

class SQLConfig(CeleryConfig):
    """ Default SQL Configuration """

    import os

    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/testing/app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db/testing/migrations/')
    
class Config(SQLConfig):
    """ Flask Configuration global to all environments """

    DEBUG = True
    TESTING = False
    SECRET_KEY = 'This is a very very secret key'

    # TODO
    MAIL_SERVER = 'smtp.localhost.test'
    MAIL_DEFAULT_SENDER = 'admin@demo.test'
    MAIL_SUPPRESS_SEND = True

class Testing(Config):
    TESTING = True

    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Production(Config):
    DEBUG = False
    MAIL_SUPPRESS_SEND = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/production/app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db/production/migrations/')

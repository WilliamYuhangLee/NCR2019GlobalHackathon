import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    """
    Config class used when environment variable ENV is set to 'production'
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Config class used when environment variable ENV is set to 'development'
    """
    DEBUG = True

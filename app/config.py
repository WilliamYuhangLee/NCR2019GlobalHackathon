class Config(object):
    pass


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

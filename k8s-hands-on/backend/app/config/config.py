class Config(object):
    pass
 
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class TestConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    'development': DevelopmentConfig,
    'test':TestConfig,
    'production':ProductionConfig
}
class Config:
    SECRET_KEY = 'secret key in AlJjam'

    @staticmethod
    def __init__(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@ip/database schema?charset=utf8'


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'product' : ProductionConfig,
    'default' : DevelopmentConfig
}
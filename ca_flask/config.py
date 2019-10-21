import os


class Config():
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somesecurekey'
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGO_DB') or 'content_aggregator',
        'host': os.environ.get('MONGO_HOST') or 'localhost',
        'port': os.environ.get('MONGO_PORT') or 27017
    }

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')



import random
import string

class Config:
    SECRET_KEY = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(60))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yellow_book.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    



class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
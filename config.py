import os
from decouple import config

class Config:
   SECRET_KEY = 'example'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/project_web2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sifuentescovarrubiasitsl@gmail.com'
    MAIL_PASSWORD = 'csc090890'
    # MAIL_PASSWORD = config('MAIL_PASSWORD')

    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
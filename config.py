class Config:
   SECRET_KEY = 'example'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/project_web2'

    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
class Config:
   SECRET_KEY = 'example'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
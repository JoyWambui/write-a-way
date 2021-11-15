import os

class Config:
    """Parent class configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_IMAGES_DEST ='app/static/images'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://bobo:Riptide@localhost/write_a_way'
    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    
class ProdConfig(Config):
    """Child class production configurations."""
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://bobo:Riptide@localhost/write_a_way_test'
class DevConfig(Config):
    """Child class production configurations."""
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://bobo:Riptide@localhost/write_a_way'
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
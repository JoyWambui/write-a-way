

class Config:
    """Parent class configurations"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://bobo:Riptide@localhost/write_a_way'

class ProdConfig(Config):
    """Child class production configurations."""
    pass


class DevConfig(Config):
    """Child class production configurations."""
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
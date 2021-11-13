from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

#Creating extensions instances
db = SQLAlchemy()


def create_app(config_name):
    """Creates the application instance under different configurations."""
    app = Flask(__name__)  
    
    #Creating app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing Flask extensions
    db.init_app(app)
    
    #Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app  
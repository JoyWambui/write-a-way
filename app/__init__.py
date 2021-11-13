from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

#Creating extensions instances
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'


def create_app(config_name):
    """Creates the application instance under different configurations."""
    app = Flask(__name__)  
    
    #Creating app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing Flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    
    #Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authentication')

    
    return app  
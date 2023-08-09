from flask import Flask

from config import Config
from app.extensions import db, bcrypt, cors, jwtmanager, csrf

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    
    # Initialize Flask extensions here
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app, origins=app.config['ALLOWED_ORIGINS'])
    jwtmanager.init_app(app)
    csrf.init_app(app)
    
    

    # Register blueprints here
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)
    


    return app

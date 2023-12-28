from flask import Flask
from app.extensions import users_db, login_manager
from app.auth import auth_bp

def create_app(config):
    """Instantiate, register and setup the Flask App instance."""
    app = Flask(__name__)

    # Configure the core APP instance
    app.config.from_object(config)

    # Initialize extensions
    users_db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(auth_bp, url_prefix='/a')

        # Setup db
        users_db.create_all()

    return app

from flask import Flask


def create_app(config):
    """Instantiate, register and setup the Flask App instance."""
    app = Flask(__name__)
    app.config.from_object(config)

    # Configure DB

    # Register Blueprints

    # Register Extensions

    return app

from os import environ, path, urandom

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, "../.env"))


class Config:
    """Flask App configuration."""

    FLASK_APP = environ.get('FLASK_APP', 'run.py')
    SECRET_KEY = environ.get('FLASK_KEY', urandom(16))

    TEMPLATES_FOLDER = 'templates'
    STATIC_FOLDER = 'static'

    DB_ENGINE = environ.get('DB_ENGINE', None)
    DB_USERNAME = environ.get('DB_USERNAME', None)
    DB_PASSWORD = environ.get('DB_PASSWORD', None)
    DB_HOST = environ.get('DB_HOST', None)
    DB_PORT = environ.get('DB_PORT', None)
    DB_NAME = environ.get('DB_NAME', None)

    try:
        SQLALCHEMY_DATABASE_URI =\
            f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    except Exception as e:
        # Fallback to sqlite3
        print("[ERROR] Exception raised: " + str(e))
        SQLALCHEMY_DATABASE_URI =\
            'sqlite3:///' + path.join(BASE_DIR, "db_local.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Flask App configuration for Development environment."""

    FASK_ENV = "development"
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    """Flask App configuration for Production environment."""

    FLASK_ENV = "production"
    FLASK_DEBUG = False


app_configurations = {
    "dev": DevConfig,
    "prod": ProdConfig
}

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user

users_db = SQLAlchemy()
login_manager = LoginManager()

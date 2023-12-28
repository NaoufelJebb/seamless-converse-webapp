from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import users_db as db


class UserModel(UserMixin, db.Model):
    """User model."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(32),
        unique=False,
        nullable=False
    )

    email = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(256),
        unique=False,
        nullable=False
    )

    created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True,
    )

    last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True,
    )

    def set_password_hash(self, password):
        """
        Create hashed password.

        Note that the default key derivation function is used (less secure).
        """
        self.password_hash = generate_password_hash(
            password,
            method='pbkdf2',
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password_hash, password)

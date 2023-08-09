import hashlib
import secrets
import string
from datetime import datetime

import bcrypt
from flask import abort
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import create_access_token
from flask_login import UserMixin, current_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db
from app.models.server import Server


class User(db.Model):
    """Represents a user in the system."""

    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    phone_number: str = db.Column(db.String(20), unique=True, nullable=True)
    phone_number_verified: bool = db.Column(db.Boolean, default=False)
    email_verified: bool = db.Column(db.Boolean, default=False)
    hashed_password: str = db.Column(db.String(100), nullable=False)
    salt: str = db.Column(db.String(100), nullable=False)
    is_admin: bool = db.Column(db.Boolean, default=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    global_banned: bool = db.Column(db.Boolean, default=False)
    role: str = db.Column(db.String(100), default="user")
    active: bool = db.Column(db.Boolean, default=True)
    api_key: str = db.Column(db.String(100), nullable=True, unique=True)
    profile_picture: str = db.Column(db.String(200), nullable=True)

    def __init__(self, username: str, email: str, password: str, phone_number: str = None,
                 is_admin: bool = False, global_banned: bool = False, role: str = "user",
                 active: bool = True, api_key: str = None, profile_picture: str = None) -> None:
        """
        Initialize a new User instance.

        Args:
            username: The username of the user.
            email: The email of the user.
            password: The password of the user.
            phone_number: The phone number of the user (default: None).
            is_admin: Whether the user is an administrator (default: False).
            global_banned: Whether the user is globally banned (default: False).
            role: The role of the user (default: "user").
            active: Whether the user account is active (default: True).
            api_key: The API key of the user (default: None).
            profile_picture: The URL or file path of the user"s profile picture (default: None).
        """
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.salt = None
        self.hashed_password = None
        self.is_admin = is_admin
        self.global_banned = global_banned
        self.role = role
        self.active = active
        self.api_key = api_key
        self.profile_picture = profile_picture

    @classmethod
    def find_by_username(cls, username: str):
        """
        Find a user by their username.

        Args:
            username: The username to search for.

        Returns:
            The user object if found, None otherwise.
        """
        return cls.query.filter_by(username=username).first()

    def create_account(self) -> str:
        """
        Create a user account.

        Returns:
            A success message indicating the account was created.
        """
        # Generate a unique salt for the user
        self.salt = bcrypt.gensalt(rounds=12).decode("utf-8")

        # Hash the password using bcrypt and the generated salt
        password_bytes = self.password.encode("utf-8")
        self.hashed_password = bcrypt.hashpw(
            password_bytes, self.salt.encode("utf-8")).decode("utf-8")

        # Hash the email using SHA-256
        email_hash = hashlib.sha256(self.email.encode()).hexdigest()

        # Store the hashed email in the database
        self.email = email_hash

        # Hash the phone number using SHA-256 if provided
        if self.phone_number:
            phone_number_hash = hashlib.sha256(
                self.phone_number.encode()).hexdigest()
            self.phone_number = phone_number_hash

        db.session.add(self)
        db.session.commit()

        # Return a success message or perform any additional tasks
        return f"Account created successfully. Username: {self.username}"

    def verify_password(self, password: str) -> bool:
        """
        Verify if the provided password matches the stored hashed password.

        Args:
            password: The password to verify.

        Returns:
            True if the password is correct,    False otherwise.
        """
        password_bytes = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(
            password_bytes, self.salt.encode("utf-8")).decode("utf-8")
        return hashed_password == self.hashed_password

    def generate_api_key(self) -> str:
        """
        Generate a random API key for the user.

        Returns:
            The generated API key.
        """
        characters = string.ascii_letters + string.digits
        api_key = "".join(secrets.choice(characters) for _ in range(32))
        self.api_key = api_key
        db.session.commit()
        return api_key

    def generate_access_token(self) -> str:
        # Generate and return an access token for the user
        access_token = create_access_token(identity=self.id)
        return access_token

    def to_dict(self) -> dict:
        """
        Convert User object to a dictionary.

        Returns:
            A dictionary representation of the User object.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone_number": self.phone_number,
            "phone_number_verified": self.phone_number_verified,
            "email_verified": self.email_verified,
            "is_admin": self.is_admin,
            "profile_picture": self.profile_picture,
        }

from typing import Optional, Union
import re
from datetime import datetime
from uuid import uuid4

from sqlalchemy import or_
from werkzeug.security import check_password_hash

from app.extensions import db, bcrypt
from app.models.user import AdvancedUser, User


from datetime import datetime
from typing import Optional
import re
import uuid
import hashlib


class UserManager:
    def hash_password(self, password):
        """
        Hashes the given password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        hashed_password = bcrypt.generate_password_hash(password, 12).decode("utf-8")
        return hashed_password

    def check_password(self, password, hashed_password):
        """
        Checks if the given password matches the hashed password.

        Args:
            password (str): The password to check.
            hashed_password (str): The hashed password to compare with.

        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        return bcrypt.check_password_hash(hashed_password, password)

    def generate_api_key(self, username, password):
        """
        Generates an API key for the given username and password.

        Args:
            username (str): The username.
            password (str): The password.

        Returns:
            str: The generated API key.
        """
        hash_object = hashlib.sha256()
        hash_object.update(username.encode())
        hash_object.update(password.encode())
        api_key = hash_object.hexdigest()
        return api_key

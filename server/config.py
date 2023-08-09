import os
from datetime import timedelta
from flask_limiter.util import get_remote_address

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@192.168.50.232:5434/IcyNetworkMain"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=30)
    RATELIMIT_KEY_FUNC = get_remote_address
    SESSION_COOKIE_DOMAIN = False
    ALLOWED_ORIGINS = ["http://192.168.50.232:3000"]
    WTF_CSRF_SECRET_KEY = os.getenv("WTF_CSRF_SECRET_KEY")
    SESSION_PERMANENT = os.getenv("SESSION_PERMANENT")
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

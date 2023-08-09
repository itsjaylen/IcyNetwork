from datetime import timedelta
import bcrypt
import hashlib
import os

from flask import Flask, abort, jsonify, make_response, request, session
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect, validate_csrf, generate_csrf
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, unset_jwt_cookies

app: Flask = Flask(__name__)
CORS(app, supports_credentials=True)
# Set a secret key for CSRF protection
app.config['SECRET_KEY'] = 'your-secret-key'
csrf = CSRFProtect(app)
# Set the key function for rate limiting
app.config['RATELIMIT_KEY_FUNC'] = get_remote_address
limiter = Limiter(app)

# Set the secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=30)
jwt = JWTManager(app)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the database instance
db: SQLAlchemy = SQLAlchemy(app)


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    hashed_password: str = db.Column(db.String(100), nullable=False)
    salt: str = db.Column(db.String(100), nullable=False)
    is_admin: bool = db.Column(db.Boolean, default=False)

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.salt = None
        self.hashed_password = None

    def create_account(self) -> str:
        # Generate a unique salt for the user
        self.salt = bcrypt.gensalt(rounds=12).decode('utf-8')

        # Hash the password using bcrypt and the generated salt
        password_bytes = self.password.encode('utf-8')
        self.hashed_password = bcrypt.hashpw(
            password_bytes, self.salt.encode('utf-8')).decode('utf-8')

        # Hash the email using SHA-256
        email_hash = hashlib.sha256(self.email.encode()).hexdigest()

        # Store the username, hashed password, hashed email, and salt in the database
        self.email = email_hash
        db.session.add(self)
        db.session.commit()

        # Return a success message or perform any additional tasks
        return f"Account created successfully. Username: {self.username}"

    def verify_password(self, password: str) -> bool:
        # Verify if the provided password matches the stored hashed password
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(
            password_bytes, self.salt.encode('utf-8')).decode('utf-8')
        return hashed_password == self.hashed_password

    def generate_access_token(self) -> str:
        # Generate and return an access token for the user
        access_token = create_access_token(identity=self.id)
        return access_token

    def to_dict(self):
        # Convert User object to a dictionary
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_admin': self.is_admin
        }


@app.errorhandler(Exception)
def handle_error(e: Exception) -> jsonify:
    # Log the error
    app.logger.error(f"An error occurred: {str(e)}")

    # Return a secure error response
    error_message = "Internal Server Error"
    response = jsonify({'error': error_message})
    response.status_code = 500
    return response


@app.route('/api/register', methods=['POST'])
@limiter.limit("10 per minute")
def register() -> jsonify:
    try:
        print(request.json)
        username: str = request.json.get('username')
        email: str = request.json.get('email')
        password: str = request.json.get('password')

        # Check if username, email, and password are provided
        if not username or not email or not password:
            error_message = "Missing username, email, or password"
            return jsonify({'error': error_message}), 400

        # Check if the email is already used
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            error_message = "Email already in use"
            return jsonify({'error': error_message}), 409

        # Check if the username is already used
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            error_message = "Username already in use"
            return jsonify({'error': error_message}), 409

        # Create a new User instance and call create_account method
        user = User(username=username, email=email, password=password)
        user.create_account()

        # Generate an access token for the user
        access_token = user.generate_access_token()

        # Return a success response with the access token
        return jsonify({'message': 'Registration successful', 'access_token': access_token}), 200

    except Exception as e:
        # Log the error and return a secure error response
        app.logger.error(f"An error occurred: {str(e)}")
        error_message = "Internal Server Error"
        return jsonify({'error': error_message}), 500


@app.route('/api/login', methods=['POST'])
@limiter.limit("10 per minute")
def login() -> jsonify:
    try:
        print(request.json)
        email: str = request.json.get('email')
        password: str = request.json.get('password')

        # Check if email and password are provided
        if not email or not password:
            error_message = "Missing email or password"
            response = jsonify({'error': error_message})
            response.status_code = 400
            return response

        csrf_token = request.headers.get('X-CSRF-TOKEN')
        validate_csrf(csrf_token)

        # Hash the provided email using SHA-256
        email_hash = hashlib.sha256(email.encode()).hexdigest()

        # Retrieve the user from the database based on the hashed email
        user = User.query.filter_by(email=email_hash).first()

        if user and user.verify_password(password):
            # Generate an access token for the user
            access_token = user.generate_access_token()

            # Store the user ID in the session
            session['user_id'] = user.id

            # Return a success response with the access token
            return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

        else:
            # Password does not match or user not found, return an error response
            error_message = "Invalid email or password"
            response = jsonify({'error': error_message})
            response.status_code = 401
            return response

    except Exception as e:
        # Log the error and return a secure error response
        app.logger.error(f"An error occurred: {str(e)}")
        error_message = "Internal Server Error"
        response = jsonify({'error': error_message})
        response.status_code = 500
        return response


@app.route('/api/protected', methods=['GET'])
def protected_route():
    # Retrieve the user ID from the session
    user_id = session.get('user_id')

    if user_id:
        # Fetch the user from the database based on the user ID
        user = User.query.get(user_id)

        if user:
            return jsonify({'user': user.to_dict()}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Unauthorized access'}), 401


@app.route('/api/logout', methods=['POST'])
def logout():
    try:
        # Perform any additional logout logic, if needed
        # For example, you could invalidate the token on the server-side or update the token's expiration time
        csrf_token = request.headers.get('X-CSRF-TOKEN')
        validate_csrf(csrf_token)

        # Clear the access token from the client-side by unsetting the JWT cookies
        response = jsonify({'message': 'Logout successful'})
        unset_jwt_cookies(response)

        session.pop('user_id', None)
        session.clear()

        return response, 200

    except Exception as e:
        # Handle the error and return an error response
        error_message = "Logout failed. Please try again."
        response = jsonify({'error': error_message})
        response.status_code = 500
        print(e)
        return response


@app.route('/api/GetUser', methods=['GET'])
def get_user():
    # Retrieve the user ID from the session
    user_id = session.get('user_id')

    if user_id:
        # Fetch the user from the database based on the user ID
        user = db.session.get(User, user_id)

        if user:
            return jsonify({'user': user.to_dict()}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Unauthorized access'}), 401


@app.route('/api/csrf-token', methods=['GET'])
@csrf.exempt
def get_csrf_token():
    csrf_token = generate_csrf()
    response = make_response(jsonify({'csrf_token': csrf_token}))
    response.set_cookie('csrf_token', csrf_token, secure=True, httponly=True,
                        samesite='Strict', max_age=timedelta(hours=1).total_seconds())
    return response


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')

from datetime import timedelta
import hashlib
from flask import jsonify, make_response, request, session
from flask_jwt_extended import unset_jwt_cookies
from app.api import bp
from app.models.user import User
from app.api.tools.utils import RouteLogger, CSRFProtect
from app.extensions import db, csrf
from flask_wtf.csrf import generate_csrf

csrf_handle = CSRFProtect()
# register loggers
logger_register = RouteLogger("/register")
logger_login = RouteLogger("/login")
logger_logout = RouteLogger("/logout")
logger_protected = RouteLogger("/protected")
logger_GetUser = RouteLogger("/GetUser")
logger_CSRF = RouteLogger("/csrf")


@bp.route('/register', methods=['POST'])
@logger_register.log
@csrf.exempt
@csrf_handle
def register() -> jsonify:
    try:
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
        print(e)
        error_message = "Registration failed. Please try again."
        return jsonify({'error': error_message}), 500


@bp.route('/login', methods=['POST'])
@logger_login.log
@csrf.exempt
@csrf_handle
def login() -> jsonify:
    email: str = request.json.get('email')
    password: str = request.json.get('password')

    # Check if email and password are provided
    if not email or not password:
        error_message = "Missing email or password"
        response = jsonify({'error': error_message})
        response.status_code = 400
        return response

    # Hash the provided email using SHA-256
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    # Retrieve the user from the database based on the hashed email
    user = User.query.filter_by(email=email_hash).first()

    if user and user.verify_password(password):
        # Generate an access token for the user
        access_token = user.generate_access_token()

        # Store the user ID in the session
        session['user_id'] = user.id
        print(session['user_id'])
        print(access_token)

        # Return a success response with the access token
        return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

    else:
        # Password does not match or user not found, return an error response
        error_message = "Invalid email or password"
        response = jsonify({'error': error_message})
        response.status_code = 401
        return response


@bp.route('/logout', methods=['POST'])
@logger_logout.log
@csrf_handle
@csrf.exempt
def logout():
    # Perform any additional logout logic, if needed
    # For example, you could invalidate the token on the server-side or update the token's expiration time
    csrf_token = request.headers.get('X-CSRF-TOKEN')
    # validate_csrf(csrf_token)

    # Clear the access token from the client-side by unsetting the JWT cookies
    response = jsonify({'message': 'Logout successful'})
    unset_jwt_cookies(response)

    session.pop('user_id', None)
    session.clear()

    return response, 200


@bp.route('/protected', methods=['GET'])
@logger_protected.log
@csrf_handle
@csrf.exempt
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


@bp.route('/GetUser', methods=['GET'])
@logger_GetUser.log
@csrf_handle
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


@bp.route('/csrf-token', methods=['GET'])
@logger_CSRF.log
@csrf.exempt
def get_csrf_token():
    csrf_token = generate_csrf()
    response = make_response(jsonify({'csrf_token': csrf_token}))
    response.set_cookie('csrf_token', csrf_token, httponly=False,
                        samesite='Strict', max_age=timedelta(hours=1).total_seconds())
    return response

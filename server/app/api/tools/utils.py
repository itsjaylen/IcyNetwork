import datetime
import json
import logging
import logging.handlers
import os
from functools import wraps

from flask import jsonify, request


class RouteLogger:
    """RouteLogger class for logging errors for a given route."""
    loggers = {}

    def __init__(self, route):
        """
        Initializes a RouteLogger object with a given route.

        Args:
            route (str): The route associated with the logger.
        """
        self.route = route

    def get_logger(self):
        """
        Retrieves or creates a logger for the associated route.

        Returns:
            logging.Logger: The logger object for the route.
        """
        if self.route not in self.loggers:
            logger = logging.getLogger(self.route)
            logger.setLevel(logging.ERROR)

            log_dir = os.path.join("logs", self.route.lstrip('/'))
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            log_path = os.path.join(log_dir, "error.log")
            rotating_handler = logging.handlers.TimedRotatingFileHandler(
                log_path,
                when='midnight',
                interval=1,
                backupCount=7
            )
            rotating_handler.setLevel(logging.ERROR)

            compress_handler = logging.handlers.RotatingFileHandler(
                log_path,
                mode='a',
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=5
            )
            compress_handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s")
            rotating_handler.setFormatter(formatter)
            compress_handler.setFormatter(formatter)

            logger.addHandler(rotating_handler)
            logger.addHandler(compress_handler)

            self.loggers[self.route] = logger

        return self.loggers[self.route]

    def log(self, func):
        """
        Decorator function that logs exceptions thrown by the decorated function.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: The decorated function.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger = self.get_logger()
                log_data = {
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "route": self.route,
                    "error": str(e),
                }
                logger.error(json.dumps(log_data), exc_info=True)
                return "An error occurred"

        return wrapper

class CSRFProtect:
    def __init__(self, error_message="Invalid CSRF token"):
        self.error_message = error_message

    def __call__(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            csrf_token = request.headers.get('X-CSRF-TOKEN')
            if csrf_token is None:
                return jsonify({'error': self.error_message}), 400
            # Add additional CSRF token validation logic here if needed
            return f(*args, **kwargs)
        return decorated_function
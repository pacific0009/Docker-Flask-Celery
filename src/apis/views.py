import logging
from flask import request, jsonify
from services.user_service import UserService
from celery_app import record_last_login
from models.login_history import LoginHistory
from services.service_error import *
logger = logging.getLogger("default")

def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.

           return a json response and an appropriate status code.
    """
    if not request.json or 'user_id' not in request.json or 'password' not in request.json:
        return "Invalid request! Missing required user credentials", 401
    try:
        user_service = UserService()
        user = user_service.login_user(request.json)
        # assign task to celery
        record_last_login.delay(user['user_id'], user['last_login'])
        return jsonify(user), 200
    except InvalidUser:
        return "User Not Exist", 400
    except InvalidCredentials:
        return "Invalid Credentials", 401
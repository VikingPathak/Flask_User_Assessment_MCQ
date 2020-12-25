from flask import Flask, session, request
from flask_restful import Resource
from models._User import _User
import logging


logger = logging.getLogger(__name__)


class User_Login(Resource):

    def post(self):

        data = request.get_json(force=True)

        if session.get('user'):
            return {
                "state": False,
                "message": "Login detected. Please logout to continue."
            }

        username = data.get('username')
        password = data.get('password')
        if not all([username, password]):
            return {
                "state": False,
                "message": "Username or(and) Password field(s) missing."
            }

        user_exists = _User.query.filter_by(Username=username).first()
        if not user_exists:
            return {
                "state": False, 
                "message": "Username does not exist. Please try again."
            }

        if not password == user_exists.Password:
            return {
                "state"  : False,
                "message": "Username and Password do not match."
            }

        logger.error(f"{username} tried to login.")

        # password = encrypt_password(password)
        session['user'] = username

        return {
            "state": True,
            "message": "Login Successful."
        }
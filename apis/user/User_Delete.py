from flask import Flask, session, request
from flask_restful import Resource
from models._User import _User
from app import db
import logging


logger = logging.getLogger(__name__)


class User_Delete(Resource):

    def post(self):

        data = request.get_json(force=True)

        username = data.get('username')
        password = data.get('password')
        if not all([username, password]):
            return {
                "state": False,
                "message": "Username or(and) Password field(s) missing."
            }
        
        logged_in_user = session.get('user')
        if logged_in_user != username:
            return {
                "state": False,
                "message": "The requested user is not logged in."
            }

        user_exists = _User.query.filter_by(Username=username).first()
        if not user_exists:
            return {
                "state"  : False, 
                "message": "Username does not exist."
            }

        if not password == user_exists.Password:
            return {
                "state"  : False,
                "message": "Username and Password do not match."
            }

        try:
            db.session.delete(user_exists)
            db.session.commit()
        except Exception as ex:
            logger.error("An error occurred while deleting the User")
            logger.error(ex)
            return {
                "state": False,
                "message": "An error occurred. Please try again."
            }

        return {
            "state": True,
            "message": "Requested User has been removed from the system."
        }
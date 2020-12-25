from flask import Flask, session, request
from flask_restful import Resource
from models import _Admin
import logging

logger = logging.getLogger(__name__)


class Admin_Login(Resource):

    def post(self):

        data = request.get_json(force=True)
        if not data.get('admin'):
            return {
                "state": False,
                "message": "No admin details found."
            }

        username = data['admin'].get('username')
        password = data['admin'].get('password')

        if not all([username, password]):
            return {
                "state": False,
                "message": "Username or Password is missing."
            }

        admin_exists = _Admin.query.filter_by(Username=username).first()
        if not admin_exists:
            return {
                "state": False, 
                "message": "Username does not exist. Please try again."
            }

        if not password == admin_exists.Password:
            return {
                "state"  : False,
                "message": "Username and Password do not match."
            }

        logger.error(f"Admin {username} tried to login.")
        session['admin'] = True

        return {
            "state": True,
            "message": "Login Successful."
        }
from flask import Flask, session, request
from flask_restful import Resource
import logging


logger = logging.getLogger(__name__)


class User_Logout(Resource):

    def get(self):

        if not session.get('user'):
            return {
                "state": True,
                "message": "No login detected. Login to continue."
            }
        
        session.pop('user')

        return {
            "state": True,
            "message": "You've been successfully logged out of the system."
        }

        
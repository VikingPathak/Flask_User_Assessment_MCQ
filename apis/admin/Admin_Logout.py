from flask import Flask, session
from flask_restful import Resource
import logging


logger = logging.getLogger(__name__)


class Admin_Logout(Resource):

    def get(self):

        if not session.get('admin'):
            return {
                "state": True,
                "message": "No Admin login found."
            }
                
        session.pop('admin')
        logger.info("Admin Logged out of the system.")
        
        return {
            "state": True,
            "message": "You've been successfully logged out of the system."
        }

        
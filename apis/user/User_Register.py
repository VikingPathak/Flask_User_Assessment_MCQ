from flask import Flask, session, request
from flask_restful import Resource
from models._User import _User
from app import db
import re
import logging


logger = logging.getLogger(__name__)


class User_Register(Resource):

    def post(self):

        data = request.get_json(force=True)

        signup_details = data.get('details')
        if not signup_details:
            return {
                "state": False,
                "message": "No Signup details found. Please try again."
            }            
        
        firstname =  signup_details.get('firstname')
        lastname  =  signup_details.get('lastname') if signup_details.get('lastname') else ''
        email_id  =  signup_details.get('email')
        username  =  signup_details.get('username')
        password  =  signup_details.get('password')

        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(email_regex, email_id)):
            return {
                "state": False,
                "message": "Please enter a valid email ID."
            }
        email_exists = _User.query.filter_by(Email_ID=email_id).first()
        if email_exists:
            return {
                "state": True,
                "message": "Email already exists. Please try with another email."
            }
        
        if not all([firstname, lastname, email_id, username, password]):
            return {
                "state": False, 
                "message": "Some fields are blank."
            }

        user_exists = _User.query.filter_by(Username=username).first()
        if user_exists:
            logger.error(f"{username} tried to re-register.")
            return {
                "state": False, 
                "message": "Username taken. Try another username."
            }

        new_user = _User(
            Firstname=firstname,
            Lastname=lastname,
            Email_ID=email_id,
            Username=username, 
            Password=password
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as ex:
            logger.error("An error occurred while registering the User")
            logger.error(ex)
            return {
                "state": False,
                "message": "An error occurred. Please try again."
            }

        return {
            "state": True,
            "message": "Registration Successful! Please login to continue."
        }
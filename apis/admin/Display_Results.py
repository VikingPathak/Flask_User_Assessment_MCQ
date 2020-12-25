from flask import Flask, session, request
from flask_restful import Resource
from sqlalchemy import text
from app import db


class Display_Results(Resource):

    def get(self):

        if not session.get('admin'):
            return {
                "state": False,
                "message": "To proceed please login with admin credentials."
            }
        
        result_dict = {}
        score_results = db.engine.execute(text(
            f"""
            SELECT DISTINCT
                CONCAT(U.Firstname, U.Lastname),
                U.Email_ID,
                S.Score
            FROM _User U JOIN Score S ON U.Username = S.Username
            """
        ))
        for row in score_results:
            result_dict.update({
                "Name"  : row[0],
                "Email" : row[1],
                "Score" : row[2]
            })

        return result_dict
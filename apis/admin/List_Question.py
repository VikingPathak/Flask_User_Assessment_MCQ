from flask import Flask, session, request
from flask_restful import Resource
from helper.admin_func import get_assessment_questions


class List_Question(Resource):

    def get(self):
       
        if not session.get('admin'):
            return {
                "state": False,
                "message": "Please login with admin credentials to continue."
            }

        file_exists, info = get_assessment_questions()
        if not file_exists:
            return info
        
        Q_data = info
        Q_data.index += 1
        result  =  Q_data.to_dict()
        result['state'] =  True
        
        return result
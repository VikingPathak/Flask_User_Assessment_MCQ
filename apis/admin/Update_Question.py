from flask import Flask, session, request
from flask_restful import Resource
import os
from helper.admin_func import get_assessment_questions

dir_ = os.getcwd() + '\\files\\'


class Update_Question(Resource):

    def post(self):

        data = request.get_json(force=True)

        if not session.get('admin'):
            return {
                "state": False,
                "message": "Please login with admin credentials to continue."
            }

        update_request = data.get('update_questions')
        if not update_request:
            return {
                "state": True,
                "message": "Nothing to update."
            }
        
        file_exists, info = get_assessment_questions()
        if not file_exists:
            return info
        
        Q_data = info
        Q_data.index += 1
        Q_no = [str(i) for i in Q_data.index]
        updated_count = 0
        for qno, updated_question in update_request.items():
            if str(qno) not in Q_no:
                continue
            qno = int(qno)
            Q_data.iat[qno-1, 0] = updated_question
            updated_count += 1

        Q_data.to_csv(dir_ + 'questions.csv', header=False, index=False)
        Q_data.to_excel(dir_ + 'questions.xlsx', header=False, index=False)

        info = f"{updated_count} Question(s) Updated."

        return {
            "state": True,
            "message": info
        }
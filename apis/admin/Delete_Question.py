from flask import Flask, session, request
from flask_restful import Resource
import os
from helper.admin_func import get_assessment_questions

dir_ = os.getcwd() + '\\files\\'


class Delete_Question(Resource):

    def post(self):

        data = request.get_json(force=True)

        if not session.get('admin'):
            return {
                "state": False,
                "message": "Please login with admin credentials to continue."
            }

        delete_request = data.get('delete_questions')
        if not delete_request:
            return {
                "state": True,
                "message": "Nothing to delete."
            }
        
        file_exists, info = get_assessment_questions()
        if not file_exists:
            return info
        
        Q_data = info
        Q_data.index += 1
        Q_no = [str(i) for i in Q_data.index]
        deleted_count = 0
        qno_drop_list = []
        for qno in delete_request:
            if str(qno) not in Q_no:
                continue
            qno = int(qno)
            qno_drop_list.append(qno-1)
            deleted_count += 1

        Q_data.drop(qno_drop_list, inplace=True)
        Q_data.reset_index(drop=True, inplace=True)
        Q_data.index += 1
        Q_data.to_csv(dir_ + 'questions.csv', header=False, index=False)
        Q_data.to_excel(dir_ + 'questions.xlsx', header=False, index=False)

        info = f"{deleted_count} Questions have been deleted."

        return {
            "state": True,
            "message": info
        }
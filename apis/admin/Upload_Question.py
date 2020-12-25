from flask import Flask, session, request
from flask_restful import Resource
import pandas as pd
import os

dir_ = os.getcwd() + '\\files\\'


class Upload_Question(Resource):

    def post(self):

        if not session.get('admin'):
            return {
                "state": False,
                "message": "Please login with admin credentials to continue."
            }

        file_ = request.files['file']
        if file_.filename.endswith('.csv'):
            Q_data = pd.read_csv(file_, header=None, names=['Questions'])
        elif file_.filename.endswith('.xlsx'):
            try:
                Q_data = pd.read_excel(file_, header=None, names=['Questions'])
            except:
                return {
                    "state": False,
                    "message": "Some dependency issue took place. Please try uploading in CSV format."
                }
        else:
            return {
                "state": False,
                "message": "Only CSV and XLSX file formats accepted."
            }

        if not len(Q_data) > 0:
            return {
                "state"   : False,
                "message" : "No Questions present. Skipping Upload."
            }
        elif len(Q_data.columns) > 1:
            return {
                "state"   : False,
                "message" : "Please upload the file with correct formatting."
            }
        
        Q_data.index += 1
        Q_data.to_csv(dir_ + 'questions.csv', header=False, index=False)
        try:
            Q_data.to_excel(dir_ + 'questions.xlsx', header=False, index=False)
        except:
            return {
                "state": True,
                "message": "CSV Upload Successful. XLSX upload caused an error due to its dependency."
            }

        return {
            "state": True,
            "message": "Upload Successful."
        }
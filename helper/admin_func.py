import os
import pandas as pd
from models import _Admin

dir_ = os.getcwd() + '\\files\\'

def get_assessment_questions():

    CSV_EXISTS = os.path.exists(dir_ + 'questions.csv')
    XLS_EXISTS = os.path.exists(dir_ + 'questions.xlsx')

    if not any([CSV_EXISTS, XLS_EXISTS]):
        return False, {
            "state": False,
            "message": "Please make sure you have uploaded the Assessment Questions."
        }

    if CSV_EXISTS:
        return True, pd.read_csv(dir_+'questions.csv', header=None, names=['Questions'])
    else:
        try:
            return True, pd.read_excel(dir_+'questions.xlsx', header=None, names=['Questions'])
        except:
            return False, {
            "state": False,
            "message": "Please make sure you have uploaded the Assessment Questions."
        }
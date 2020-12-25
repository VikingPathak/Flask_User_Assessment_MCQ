from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import pymysql
import logging
import datetime
from app.config import DATABASE

##### APP CONFIG #####
logging.basicConfig(
    filename =  "info.log",
    level    =  logging.DEBUG,
    format   =  '%(asctime)s | %(levelname)s | %(name)s:%(lineno)s : %(message)s',
    datefmt  =  '%m-%d-%Y::%I:%M:%S %p'
)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime = datetime.timedelta(minutes=60)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

##### USER ROUTES #####
from apis.user import (
    Submit_Response,
    User_Delete,
    User_Login,
    User_Logout,
    User_Register
)
api.add_resource(User_Register, '/user/register')

api.add_resource(User_Delete, '/user/delete')

api.add_resource(User_Login, '/user/login')

api.add_resource(User_Logout, '/user/logout')

api.add_resource(Submit_Response, '/user/submit')

##### ADMIN ROUTES #####
from apis.admin import (
    Admin_Login,
    Admin_Logout,
    Delete_Question,
    Display_Results,
    List_Question,
    Update_Question,
    Upload_Question
)
api.add_resource(Upload_Question, '/admin/upload-file')

api.add_resource(List_Question, '/admin/view-questions')

api.add_resource(Update_Question, '/admin/update-file')

api.add_resource(Delete_Question, '/admin/delete-question')

api.add_resource(Display_Results, '/admin/display-results')

api.add_resource(Admin_Login, '/admin/login')

api.add_resource(Admin_Logout, '/admin/logout')
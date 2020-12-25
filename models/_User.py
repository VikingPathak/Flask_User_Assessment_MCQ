from flask_sqlalchemy import SQLAlchemy
from app import db


class _User(db.Model):

    __tablename__ = '_User'

    User_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Firstname = db.Column(db.String(255), nullable=False)
    Lastname = db.Column(db.String(255), default='')
    Email_ID = db.Column(db.String(255), nullable=False, unique=True)
    Username = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)

db.create_all()
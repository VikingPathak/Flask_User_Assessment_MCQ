from flask_sqlalchemy import SQLAlchemy
from app import db


class Score(db.Model):

    __tablename__ = 'Score'

    SID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(255), unique=True, nullable=True)
    Score = db.Column(db.Integer, nullable=False)

db.create_all()
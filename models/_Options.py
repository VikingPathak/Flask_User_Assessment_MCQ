from flask_sqlalchemy import SQLAlchemy
from app import db


class _Options(db.Model):

    __tablename__ = '_Options'

    OID    = db.Column(db.Integer, primary_key=True)
    Option = db.Column(db.String(255), nullable=False)
    Score  = db.Column(db.Integer, nullable=False)

db.create_all()
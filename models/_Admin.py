from flask_sqlalchemy import SQLAlchemy
from app import db


class _Admin(db.Model):

    __tablename__ = '_Admin'

    Username = db.Column(db.String(255), primary_key=True)
    Password = db.Column(db.String(255), nullable=False)

db.create_all()
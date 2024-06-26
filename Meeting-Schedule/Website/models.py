from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.String(150), db.ForeignKey('role.role'))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_avatar = db.Column(db.String(150), default='default.jpg')



class Role (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(150), unique=True)



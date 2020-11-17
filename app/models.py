from . import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64))
    username = db.Column(db.String(32), unique=True, index=True)
    phone_number = db.Column(db.String(20))
    confirm = db.Column(db.Boolean)
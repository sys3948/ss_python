from . import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64))
    username = db.Column(db.String(32), unique=True, index=True)
    phone_number = db.Column(db.String(20))
    confirm = db.Column(db.Boolean, default=False)

    tasks = db.relationship('Task', backref = 'author', lazy='dynamic')

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id', primary_key = True)
    title = db.Column(db.String(128))
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    comment_path = db.Column(db.String(256))
    review_path = db.Column(db.String(256))
    log_path = db.Column(db.String(256))
    checked = db.Column(db.Boolean, default=False)
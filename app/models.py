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

    alarms = db.relationship('User', backref = 'todo', lazy='dynamic')

class Alarm(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey('Task.task_id', primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Task.user_id', primary_key = True)
    email = db.Column(db.Boolean, default = False)
    kakao = db.Column(db.Boolean, default = False)
    line = db.Column(db.Boolean, default = False)
    f_message = db.Column(db.Boolean, default = False)
    instar_dm = db.Column(db.Boolean, default = False)
    twitter_dm = db.Column(db.Boolean, default = False)
    sms = db.Column(db.Boolean, default = False)
    default = db.Column(db.Boolean, default = False)

    alarm_times = db.relationship('User', backref = 'todo_alarm', lazy='dynamic')

class Alarm_time(db.Model):
    alarm_id = db.Column(db.Integer, primary_key = True)
    task_id = db.Column(db.Integer, db.ForeignKey('Alarm.task_id', primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Alarm.user_id', primary_key = True)
    time = db.Column(db.DateTime())
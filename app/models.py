from . import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64), nullable = False)
    username = db.Column(db.String(32), nullable = False, unique=True, index=True)
    phone_number = db.Column(db.String(20), nullable = False)
    confirm = db.Column(db.Boolean, default=False)

    tasks = db.relationship('Task', backref = 'author', lazy='dynamic')
    tasks_sharing = db.relationship('Task', backref = 'user', lazy = 'dynamic')


class Task(db.Model):
    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key = True)
    title = db.Column(db.String(128), nullable=False)
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    comment_path = db.Column(db.String(256))
    review_path = db.Column(db.String(256))
    log_path = db.Column(db.String(256))
    checked = db.Column(db.Boolean, default=False)


    tasks_sharing = db.relationship('Task_sharing', backref = 'task', lazy = 'dynamic')
    alarms = db.relationship('Alarm', backref = 'todo', lazy='dynamic')


class Task_sharing(db.Model):
    __tablename__ = 'task_sharing'
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('task.user_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    level = db.Column(db.Integer)


class Contents(db.Model):
    __tablename__ = 'contents'
    contents_id = db.Column(db.Integer, primary_key = True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('task.user_id'), primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    level = db.Column(db.Integer)


class Alarm(db.Model):
    __tablename__ = 'alarm'
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('task.user_id'), primary_key = True)
    email = db.Column(db.Boolean, default = False)
    kakao = db.Column(db.Boolean, default = False)
    line = db.Column(db.Boolean, default = False)
    f_message = db.Column(db.Boolean, default = False)
    instar_dm = db.Column(db.Boolean, default = False)
    twitter_dm = db.Column(db.Boolean, default = False)
    sms = db.Column(db.Boolean, default = False)
    default = db.Column(db.Boolean, default = False)

    alarm_times = db.relationship('Alarm_time', backref = 'todo_alarm', lazy='dynamic')


class Alarm_time(db.Model):
    __tablename__ = 'alarm_time'
    alarm_id = db.Column(db.Integer, primary_key = True)
    task_id = db.Column(db.Integer, db.ForeignKey('alarm.task_id'), primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('alarm.user_id'), primary_key = True)
    time = db.Column(db.DateTime())


from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate
from app.models import User, Task, Task_sharing, Contents, Alarm, Alarm_time

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app = app, db = db, User = User, Task = Task, Task_sharing = Task_sharing, Contents = Contents, Alarm = Alarm, Alarm_time = Alarm_time)

# if __name__ == "__main__":
#     manager.run(debug=True)
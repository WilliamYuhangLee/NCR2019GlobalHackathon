from flask_script import Shell, Manager, prompt_bool, prompt
from flask_migrate import MigrateCommand

from app import create_app, db
from run import app
from app.gym import models


manager = Manager(create_app)
manager.add_command("db", MigrateCommand)


def _make_context():
    return dict(app=app, db=db, models=models)


manager.add_command("shell", Shell(make_context=_make_context))


@manager.command
def initdb():
    db.create_all()
    print("All tables have been created.")


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()

if __name__ == "__main__":
    manager.run()

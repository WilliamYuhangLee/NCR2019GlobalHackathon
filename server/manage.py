from flask_script import Shell, Manager
from flask_migrate import MigrateCommand

from app import create_app, db
from run import app
from app.gym import models


manager = Manager(create_app)
manager.add_command("db", MigrateCommand)


def _make_context():
    return dict(app=app, db=db, models=models)


manager.add_command("shell", Shell(make_context=_make_context))


if __name__ == "__main__":
    manager.run()

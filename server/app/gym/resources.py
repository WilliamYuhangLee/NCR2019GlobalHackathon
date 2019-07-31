from flask_restful import Resource
from flask_restful import current_app as app


class Todo(Resource):

    def get(self):
        return app.config['SQLALCHEMY_DATABASE_URI']

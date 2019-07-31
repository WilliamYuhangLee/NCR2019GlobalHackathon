from flask import jsonify
from flask_restful import Resource
from flask_restful import current_app as app
from . import api


class Stats(Resource):

    def get(self, timeframe):
        example = {
            'message': "Success.",
            'status': 200,
            'data': {
                0: 10,
                1: 20,
                2: 20,
                3: 30,
                4: 40,
                5: 50,
                6: 60,
            }
        }
        if timeframe == 'week':
            return jsonify(example)


api.add_resource(Stats, '/stats/<string:timeframe>')

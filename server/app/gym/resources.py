from flask import jsonify
from flask_restful import Resource
from . import api
from .models import Visit

import datetime as dt


def respond(message='Success', status=200, data=None):
    json = {
        'message': message,
        'status': status,
    }
    if data:
        json['data'] = data
    return jsonify(json)


class Stats(Resource):

    def get(self, timeframe):
        if timeframe == 'week':
            today = dt.date.today()
            data = {}
            for i in range(1, 8):
                date = today - dt.timedelta(days=i)
                count = Visit.count_by_day(date)
                data[str(date)] = count
            return respond(data=data)


api.add_resource(Stats, '/stats/<string:timeframe>')

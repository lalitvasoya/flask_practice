from flask.views import MethodView
from flask import jsonify


class ApiTest(MethodView):

    def get(self):
        return jsonify({"status": "Docker and jenkins deployed!!!!!!"})

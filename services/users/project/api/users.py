# services/users/project/api/users.py

from flask import Blueprint
from flask_restful import Resource, Api

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

# create our own "Resource" class by extending Resource. UsersPing extends Resource
class UsersPing(Resource):
	def get(self):
		return {
			'status': 'success',
			'message': 'pong!'
		}

api.add_resource(UsersPing, '/users/ping')

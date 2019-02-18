from flask_restful import Api
from app import app
from api.user import UsersApi, UserApi

api = Api(app)

api.add_resource(UsersApi, '/users', "/users")
api.add_resource(UserApi, '/users/<user_name>')


from flask_restful import Api
from app import app
from api.user import UserApi

api = Api(app)

api.add_resource(UserApi, '/users')

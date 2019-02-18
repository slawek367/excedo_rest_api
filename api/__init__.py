from flask_restful import Api
from app import app
from api.user import UsersApi, UserApi
from api.profile_photo import ProfilePhotoApi

api = Api(app)

api.add_resource(UsersApi, '/users', "/users")
api.add_resource(UserApi, '/users/<user_name>')
api.add_resource(ProfilePhotoApi, '/users/<user_name>/profile_photo')
import os
from config import ProductionConfig
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', ProductionConfig))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

from model import user

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username')
parser.add_argument('password', type=str, help='Password')
parser.add_argument('email', type=str, help='Email')

class UserApi(Resource):
    def get(self):
        users = user.User.query.all()
        users_list = [u.serialize for u in users]
        return jsonify(users_list)
    
    def post(self):
        args = parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']

        u = user.User(username, email, password)
        db.session.add(u)
        print(db.session.commit())
        return f'User {username} created'

api.add_resource(UserApi, '/users')

if __name__ == '__main__':
    app.run()


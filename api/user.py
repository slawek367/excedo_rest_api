from flask_restful import Resource, reqparse
from flask import jsonify
from model.user import User
from app import db

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username')
parser.add_argument('password', type=str, help='Password')
parser.add_argument('email', type=str, help='Email')

class UserApi(Resource):
    def get(self):
        users = User.query.all()
        users_list = [u.serialize for u in users]
        return jsonify(users_list)
    
    def post(self):
        args = parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']

        u = User(username, email, password)
        db.session.add(u)
        print(db.session.commit())
        return f'User {username} created'
import re
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

        user_not_valid, code = check_username_is_not_valid(username)
        if user_not_valid:
            return user_not_valid, code

        email_not_valid, code = check_email_is_not_valid(email)
        if email_not_valid:
            return email_not_valid, code

        u = User(username, email, password)
        db.session.add(u)
        db.session.commit()
        return {"msg": f'User {username} created'}

def check_username_is_not_valid(username):
    if not username:
        return {"error": "username field is missing"}, 400
    if len(username) > 30:
        return {"error": f"Username {username} is too long"}, 400
    if User.query.filter_by(username=username).first():
        return {"error": f"Username {username} already exists"}, 409
    return False, 200

def check_email_is_not_valid(email):
    if not email:
        return {"error": "email field is missing"}, 400
    if len(email) > 40:
        return {"error": f"Email {email} is too long"}, 400
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return {"error": f"Email {email} is wrong"}, 422
    if User.query.filter_by(email=email).first():
        return {"error": f"Email {email} is already used"}, 409
    return False, 200

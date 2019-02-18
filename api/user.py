import re
from flask_restful import Resource, reqparse
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from model.user import User
from app import db

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username')
parser.add_argument('password', type=str, help='Password')
parser.add_argument('email', type=str, help='Email')

parser2 = reqparse.RequestParser()
parser2.add_argument('email', type=str, help='Email', store_missing=False)
parser2.add_argument('old_password', type=str, help='Old password', store_missing=False)
parser2.add_argument('new_password', type=str, help='New password', store_missing=False)

class UserApi(Resource):
    def get(self, user_name):
        user = User.query.filter_by(username=user_name).first()
        if user:
            return jsonify(user.serialize)
        else:
            return {"error": f'User {user_name} does not exists'}, 404
    
    def put(self, user_name):
        args = parser2.parse_args()
        user = User.query.filter_by(username=user_name).first()
        if user:
            print(args)
            if "email" in args:
                email = args['email']
                email_not_valid, code = check_email_is_not_valid(email, True)
                if email_not_valid:
                    return email_not_valid, code
                user.email = email
                db.session.commit()
                return {"msg": "Email was updated"}
            elif "old_password" in args and "new_password" in args:
                old_password = args['old_password']
                new_password = args['new_password']

                if check_password(user.password, old_password):
                    password_not_valid, code = check_password_is_not_valid(new_password)
                    if password_not_valid:
                        return password_not_valid, code
                    user.password = set_password(new_password)
                    db.session.commit()
                    return {"msg": "Password changed"}, 200
                else:
                    return {"error": "Old password is wrong"}, 400
            else:
                return {"error": "No parameters provided"}, 400

class UsersApi(Resource):
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

        password_not_valid, code = check_password_is_not_valid(password)
        if password_not_valid:
            return password_not_valid, code

        u = User(username, email, set_password(password))
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

def check_email_is_not_valid(email, update=False):
    if not email:
        return {"error": "email field is missing"}, 400
    if len(email) > 40:
        return {"error": f"Email {email} is too long"}, 400
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return {"error": f"Email {email} is wrong"}, 422
    if not update and User.query.filter_by(email=email).first():
        return {"error": f"Email {email} is already used"}, 409
    return False, 200

def check_password_is_not_valid(password):
    if not password:
        return {"error": "password field is missing"}, 400
    if len(password) < 6:
        return {"error": f"Password {password} is too short"}, 400
    if len(password) > 30:
        return {"error": f"Password {password} is too long"}, 400
    return False, 200

def set_password(password):
    return generate_password_hash(password)

def check_password(pw_hash, password):
    return check_password_hash(pw_hash, password)
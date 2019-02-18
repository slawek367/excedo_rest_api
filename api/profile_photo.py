from flask_restful import Resource, reqparse
from flask import jsonify
import werkzeug
from model.profile_photo import ProfilePhoto
from model.user import User
from app import db

parser = reqparse.RequestParser()
parser.add_argument('photo', type=werkzeug.datastructures.FileStorage, location='files')

class ProfilePhotoApi(Resource):
    
    def get(self, user_name):
        user = User.query.filter_by(username=user_name).first()
        if user:
            photo = ProfilePhoto.query.filter_by(user_id=user.id).first()
            if photo:
                return jsonify(photo.serialize)
        return {"error": f"User {user_name} does not exists"}, 404
    
    def post(self, user_name):
        args = parser.parse_args()
        user = User.query.filter_by(username=user_name).first()

        if user:
            profile_photo = args['photo']
            url = upload_to_s3(profile_photo, user_name)
            if url:
                photo = ProfilePhoto(url, user.id)
                db.session.add(photo)
                db.session.commit()
                return {"msg": f"Profile photo saved", "url": url}, 200
            else:
                return {"msg": f"Something went wrong"}, 400
            #profile_photo.save(f"{user_name}_profile_photo.jpg")
            return "ok"
        return {"error": f"User {user_name} not exists"}, 404

def upload_to_s3(profile_photo, user_name):
    return f"url_to_{user_name}_profile_photo.jpg"
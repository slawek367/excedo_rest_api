from app import db

class ProfilePhoto(db.Model):
    __tablename__ = "profile_photos"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, url, user_id):
        self.url = url
        self.user_id = user_id

    def __repr__(self):
        return f'Profile photo {self.url}'

    @property
    def serialize(self):
       return {
           'id' : self.id,
           'user_id': self.user_id,
           'url': self.url
       }

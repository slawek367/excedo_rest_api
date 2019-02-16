import datetime
from app import db
from datetime import datetime

def dump_datetime(value):
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'User {self.username}'

    @property
    def serialize(self):
       return {
           'id' : self.id,
           'username': self.username,
           'created': dump_datetime(self.created),
           'email': self.email
       }
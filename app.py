import os
from config import ProductionConfig
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', ProductionConfig))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import api

if __name__ == '__main__':
    app.run()
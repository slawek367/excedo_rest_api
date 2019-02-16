from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
import os
import config
import logging

logger = logging.getLogger('app_logger')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

FLASK_ENV = os.environ.get("FLASK_ENV", default=False)
if FLASK_ENV and FLASK_ENV == "development":
    logger.setLevel(logging.DEBUG)
    logger.debug("Starting development server")
    logger.debug("Used DB: {}".format(app.config['SQLALCHEMY_DATABASE_URI']))
else:
    logger.setLevel(logging.INFO)

db = SQLAlchemy(app)
import api

if __name__ == '__main__':
    app.run()
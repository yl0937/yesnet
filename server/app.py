import uuid

from flask import Flask, jsonify, request
from yesnet.server.controller.views import view
from yesnet.server.controller.api import api_page
from flask_cors import CORS, cross_origin
from yesnet.server.models.database import ZenMongo
# instantiate the app


app = Flask(__name__)
CORS(app, resources={r'*':{'origins':'*'}})
app.config.from_object(__name__)


def add_blueprint(app):
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(api_page, url_prefix='/api')

    # DB connect
    zen_mongo = ZenMongo()
    api_page.resource['mongo'] = zen_mongo
    view.resource['mongo'] = zen_mongo


# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# configuration
DEBUG = True

# sanity check route

if __name__ == '__main__':
    app.run(host='0.0.0.0')

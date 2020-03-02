import uuid

from flask import Flask, jsonify, request
from yesnet.server.controller.views import view
from yesnet.server.controller.api import api_page
from flask_cors import CORS, cross_origin

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(view, url_prefix='/')
app.register_blueprint(api_page, url_prefix='/api')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# configuration
DEBUG = True

# sanity check route

if __name__ == '__main__':
    app.run(host='0.0.0.0')

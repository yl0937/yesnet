from flask import Blueprint, jsonify, request, render_template, abort
from jinja2 import TemplateNotFound
import json

from bson import json_util
from flask import Blueprint, render_template, abort, jsonify, request, redirect, session, url_for
from flask import current_app as app
# import bcrypt
from pymongo import MongoClient, collection

from server.controller import redisfunction
from server.models.database import ZenMongo
from server.models.dom import DApp

from server.utils import zen_util
from functools import wraps
from datetime import timedelta, datetime
import jwt
from flask import Response
from server.models.dom import User


view = Blueprint('view', __name__, template_folder='template')


@view.route('/', methods=['GET'])
def get_main():
    return render_template('index.html')

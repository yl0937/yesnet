import datetime

from flask import Blueprint, request, Response, jsonify
import jwt

login_page = Blueprint('login_page', __name__)


@login_page.route('/login', methods=['POST'])
def login():
    return jsonify({
        'code': 200,
        'access_token' : 'token'
    })


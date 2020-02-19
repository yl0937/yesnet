from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/tiki', methods=['GET'])
def tiki_taka():
    return jsonify('Taka!')

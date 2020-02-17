from flask import Blueprint, jsonify

api = Blueprint('api', __name__, static_url_path='/api')


@api.route('/tiki', methods=['GET'])
def tiki_taka():
    return jsonify('taka!')
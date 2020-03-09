# import json

from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

from flask import Response
from . import redisfunction

view_page = Blueprint('view_page', 'view_page', template_folder='templates')
view_page.resource = {}


@view_page.route('/', methods=['GET'])
def get_main():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/dashboard', methods=['GET'])
def push_dashboard():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/launch', methods=['GET'])
def push_launch():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/login', methods=['GET'])
def push_login():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/register', methods=['GET'])
def push_register():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/dappslaunch', methods=['GET'])
def push_dappslunch():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/dappsupload', methods=['GET'])
def push_dappsupload():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/dappslist', methods=['GET'])
def push_dappslist():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/users', methods=['GET'])
def push_users():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/watchblock', methods=['GET'])
def push_watchblock():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/watchtx', methods=['GET'])
def push_watchtx():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/viewdapp', methods=['GET'])
def push_viewdapp():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@view_page.route('/node', methods=['GET'])
def push_node():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
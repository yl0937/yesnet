from flask import Blueprint, render_template

index_blueprint = Blueprint('index', '__name__', url_prefix="index")


@index_blueprint.route("/")
def index():
  return "Hello World!"

@index_blueprint.route("/yihi")
def yihi():
  return "ugu chu"

from . import main
from flask import jsonify


@main.route('/')
def index():
    return '''Index Flask App'''
#!/usr/bin/python3
""""""


from flask import  Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views

from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def errorhandler(error):
    """http request"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    Apihost = getenv('HBNB_API_HOST', default='0.0.0.0')
    Apiport = getenv('HBNB_API_PORT', default='5000')
    app.run(host=Apihost, port=Apiport, threaded=True)

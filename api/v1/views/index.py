#!/usr/bin/python3
"""Flask applicattion that retrieves information"""


from flask import jsonify
from models import storage
from api.v1.views import app_views



@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """status of API"""
    return jsonify({"status": "OK"})



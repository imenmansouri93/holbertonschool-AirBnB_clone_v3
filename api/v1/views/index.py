#!/usr/bin/python3
""""""
from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State


@app_views.route('/status', strict_slashes=False)
def status():
    """status of API"""
    return jsonify({"status": "OK"})
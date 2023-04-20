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
import json 


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """status of API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """"""
    dict = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }
    json_dict = json.dumps(dict, indent=2)
    return json_dict

#!/usr/bin/python3
"""

Flask applicationfor city class/entity
"""

from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=["GET"], strict_slashes=False)
def retrievesAllCties(state_id):
    """return the list of all city objects"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)
    cities = state.cities
    cities_list = []
    for city in cities:
        cities_list.append(city.to_dict())
        return jsonify(cities_list)
    

@app_views.routes("/cities/<city_id>", methods=["GET"], strict_slashes=False)
def retrivesCityById(city_id):
    """return an  object by Id"""
    city = storage.get(City, city_id)

    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.routes("/cities/<city_id>", methods=["DELETE"], strict_slashes=False)
def deleteCityById(city_id):
    """delete an object by Id"""
    city = storage.get(City, city_id)

    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=["POST"], strict_slashes=False)
def postCity(state_id):
    """create an object"""
    city_data = request.get_json()
    state = storage.get(State, state_id)
    
    if not city_data:
        abort(400, 'Not json')
    if not state:
        abort(404)
    if "name" not in city_data:
        abort(400, 'Missing name')

    new_city = City(**city_data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route("cities/<city_id>", methods=["PUT"], strict_slashes=False)
def updateCity(city_id):
    """update an object """
    city = storage.get(City, city_id)
    city_data = request.get(City, city_id)

    if not city:
        abort(404)
    if city is not city_data:
        abort(400, "Not a JSON")

    for key, value in city_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200

        
    
    

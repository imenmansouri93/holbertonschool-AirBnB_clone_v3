#!/usr/bin/python3
"""Flask apllication 
for state class/entity
"""

from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City
from models.amenity import Amenity


@app_views.route("/amenities", methods=["GET"], strict_slashes=False)
def retrievesAllAmenities():
    """
    retrieve all objects
    """
    amenities = storage.all(amenities).values()
    amenities_list = []
    for amenity in amenities:
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list)


@app_views.route("/amenities/<amenity_id>", methods=["GET"], strict_slashes=False)
def retriveAminityById(amenity_id):
    """
    retrieves object By Id
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", methods=["DELETE"], strict_slashes=False)
def deleteAmenityById(amenity_id):
    """
    delte an obeject by id
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def postAmenity():
    amenity_data = request.get_json()
    if not amenity_data:
        abort(400, 'Not a JSON')
    if "name"  not in amenity_data:
        abort(404, "Missing name")
    new_amenity = Amenity(**amenity_data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", methods=["PUT"], strict_slashes=False)
def updateObject(amenity_id):
    """"""
    amenity_data = request.get_json()
    amenity = storage.get(Amenity, amenity_id)
    if not  amenity:
        abort(404)

    if not amenity_data:
        abort(400, "Not a JSON")

    for key, value  in amenity_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200

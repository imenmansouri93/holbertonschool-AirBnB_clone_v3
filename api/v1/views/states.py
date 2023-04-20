#!/usr/bin/python3
"""Flask apllication 
for state class/entity
"""


from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def retrievesAllStates():
    """returns the list of all Statee objects"""
    states = storage.all(states).values()
    states_list = []
    for state in states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def getStateById(state_id):
    """return an object by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify((state.to_dict()))


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def deleteStateById(state_id):
    """delete an object by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def postState():
    """Create an object"""
    state_data = request.get_json()
    if not state_data:
        abort(400, "Not a JSON")
    new_state = State(**state_data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def ubdateState(state_id):
    """ubdate an objects"""
    state_data = request.get_json()
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    elif not  state_data:
        abort(400, "Not a JSON")

    for key, value in state_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
#!/usr/bin/python3
"""Flask application for user class/entity"""
from api.v1.views import app_views
from models import storage
from models.user import User
from flask import jsonify, abort, request


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def retrivesAllUsers():
    """returns the list of all User objects"""
    users = storage.all(User).values()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def getUserById(user_id):
    """Returs an objects by id"""
    user = storage.gett(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def deleteUserById(user_id):
    """Delete  an objects By Id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route("/users", methods=["POST"], strict_slashes=False)
def createUser():
    """Create an object"""
    user_data = request.get_json()
    if not user_data:
        abort(400, "Not a JSON")
    elif "email" not in user_data:
        abort(400, "Missing  email")
    elif "password" not in user_data:
        abort(400, "Missing  password")
    new_user = User(**user_data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def updateUser(user_id):
    """update an object"""
    user_data = request.get_json()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    elif not user_data:
        abort(400, "Not a JSON")

    for key, value in user_data.items():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
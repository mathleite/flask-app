from flask import Blueprint, request
from user.models.user_model import UserModel
from utils.response import Response
from playhouse.shortcuts import model_to_dict
from utils.hash_maker import HashMaker

user_routes_blueprint = Blueprint('user', __name__)


@user_routes_blueprint.route('/user', methods=['GET'])
def get_all():
    users: list = []

    for row in UserModel.select().dicts():
        users.append(row)

    return Response.create(status_code=200, response=users)


@user_routes_blueprint.route('/user', methods=['POST'])
def create():
    content = request.get_json()
    try:
        user: UserModel = UserModel(
            name=content['name'],
            password=HashMaker.create_hash(content['password'])
        )

        if user.save():
            return Response.create(status_code=201, response='User saved successfully!')
        return Response.create(status_code=500, response='User not saved!')
    except Exception as exception:
        return Response.create(status_code=500, response=str(exception))


@user_routes_blueprint.route('/user/<user_id>', methods=['POST', 'PUT'])
def update_user(user_id):
    try:
        user = UserModel.get_by_id(user_id)
    except:
        return Response.create(status_code=404, response='User not found!')
    
    content = request.get_json()
    try:
        user.name = content['name']
        user.password = HashMaker.create_hash(content['password'])
        if user.save():
            return Response.create(status_code=201, response=model_to_dict(user))
    except:
        return Response.create(status_code=500, response='Invalid body content!')

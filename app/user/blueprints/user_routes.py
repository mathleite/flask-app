from flask import Blueprint, request
from user.models.user_model import UserModel
from utils.response import Response
from playhouse.shortcuts import model_to_dict

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
        user: UserModel = UserModel(name=content['name'], password=content['password'])
    except:
        Response.create(status_code=500, response='Invalid body content!')

    if user.save():
        return Response.create(status_code=201, response='User saved successfully!')
    return Response.create(500, 'User not saved!')


@user_routes_blueprint.route('/user/<user_id>', methods=['POST', 'PUT'])
def update_user(user_id):
    try:
        user = UserModel.get_by_id(user_id)
    except:
        return Response.create(status_code=404, response='User not found!')
    
    content = request.get_json()
    try:
        user.name = content['name']
        user.password = content['password']
        if user.save():
            return Response.create(status_code=201, response=model_to_dict(user))
    except:
        return Response.create(status_code=500, response='Invalid body content!')

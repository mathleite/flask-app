from flask import Blueprint
from user.models.user_model import UserModel
from utils.response import Response

user_routes_blueprint = Blueprint('user', __name__)


@user_routes_blueprint.route('/user', methods=['GET'])
def get_all():
    return Response.create(200, db_session.query(UserModel).all())


@user_routes_blueprint.route('/user', methods=['POST'])
def create():
    db_session.execute(db_session.insert().values(name='Matheus', password='Leite'))

    return Response.create(200, db_session.query(UserModel).all())

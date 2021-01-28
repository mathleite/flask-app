from flask import Flask
from user.blueprints.user_routes import user_routes_blueprint
from database.postgresql.postgresql import PostgreSql


def create_app(app_name: str, config_filename: str = ''):
    app = Flask(app_name)
    if config_filename:
        app.config.from_json(config_filename)

    database = PostgreSql()

    if not database.connect():
        raise Exception('Database not connected!')

    app.register_blueprint(user_routes_blueprint)

    return app

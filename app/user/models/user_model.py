from peewee import CharField, DateTimeField, IntegerField, ForeignKeyField

from database.postgresql.models.postgresql_model import PostgreSqlModel
from utils.date import Date


class UserModel(PostgreSqlModel):
    name: CharField = CharField()
    password: CharField = CharField()
    created_at: DateTimeField = DateTimeField(default=Date.get_current_datetime())

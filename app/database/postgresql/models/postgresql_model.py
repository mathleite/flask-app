from database.postgresql.postgresql import PostgreSql

from peewee import Model


class PostgreSqlModel(Model):
    class Meta:
        database = PostgreSql().get_database()

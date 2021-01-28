from os import getenv
from typing import Optional

from peewee import PostgresqlDatabase


class PostgreSql:
    def __init__(self):
        self.database: PostgresqlDatabase = PostgresqlDatabase(
            database=getenv('POSTGRES_DB'),
            user=getenv('POSTGRES_USER'),
            password=getenv('POSTGRES_PASSWORD'),
            host=getenv('POSTGRES_HOST'),
            port=getenv('POSTGRES_PORT')
        )

    def get_database(self) -> PostgresqlDatabase:
        return self.database

    def connect(self) -> bool:
        return self.database.connect()


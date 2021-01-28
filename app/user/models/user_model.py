from sqlalchemy import Integer, Column, String, DateTime

from database.postgresql.postgresql import Base
from utils.date import Date


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    password = Column(String(50))
    created_at = Column(DateTime, default=Date.get_current_datetime())

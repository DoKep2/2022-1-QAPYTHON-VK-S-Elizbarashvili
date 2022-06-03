from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    middle_name = Column(String(255), default=None)
    username = Column(String(16), default=None, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    access = Column(SmallInteger, default=None)
    active = Column(SmallInteger, default=None)
    start_active_time = Column(DateTime, default=None)

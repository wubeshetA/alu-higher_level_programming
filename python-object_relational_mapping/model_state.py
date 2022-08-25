#!/usr/bin/python3
"""A script that contains State models that used to create a table."""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

host = 'localhost'
username = argv[1]
passwd = argv[2]
port = 3306
db_name = argv[3]
engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                       .format(username, passwd, host, port, db_name))

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base class.
    It is a model to create a table in a database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

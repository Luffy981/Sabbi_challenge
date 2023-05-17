#!/usr/bin/env python3

from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from os import getenv
from models.basemodel import Base

# Format: dialect+driver://username:password@host:port/database
sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
user = "luffy"
pssw = getenv('DB_MYSQL_PWD')
host = "localhost"
db = "sabbi"

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Connection to database """
        self.__engine = create_engine(sql.format(user, pssw, host, db),
                                      pool_pre_ping=True)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def reload(self):
        """ Reload session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__enginew, expire_on_commit=False)
        self.__session = session()

    def close(self):

        """ Close session """
        self.__session.close()

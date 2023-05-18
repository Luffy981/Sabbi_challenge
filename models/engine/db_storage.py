#!/usr/bin/env python3

from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from os import getenv
from models.basemodel import Base
from models.user import User
import models


# Format: dialect+driver://username:password@host:port/database
sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
user = getenv('DB_MYSQL_USR') # sabbi_dev
pssw = getenv('DB_MYSQL_PWD') # sabbi_pwd
host = getenv('DB_MYSQL_HOST') # localhost
db = getenv('DB_MYSQL_DB') # sabbi_db

classes = {"User": User}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Connection to database """
        self.__engine = create_engine(sql.format(user, pssw, host, db),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[cls] or cls is clss:
                objs = self.session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reload session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session()

    def close(self):

        """ Close session """
        self.__session.close()

    def get(self, cls, id):
        """ Returns the object based on the class name and its ID, or
        None if not found"""
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        all_class = classes.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

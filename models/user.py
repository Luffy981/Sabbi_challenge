#!/usr/bin/env python3

""" Hold class User """

import models
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """ Table representation of a user """
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    status = Column(Boolean, default=True, nullable=True)

    def __init__(self, *args, **kwargs):
        """ Init user """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """ Sets a password with md5 encryption """
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)



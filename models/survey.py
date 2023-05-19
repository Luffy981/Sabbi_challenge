#!/usr/bin/env python3
""" Survey table """

import models
from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from hashlib import md5


class Survey(BaseModel, Base):
    """ Table representation of a user """
    __tablename__ = 'survey'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    total_calculated = Column(Integer, nullable=True)
    result = Column(String(600), nullable=True)
    recomendation = Column(String(600), nullable=True)

    # Foreign key
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)

    # relationship: one to one
    user = relationship("User", backref=backref('survey', uselist=False))

    def __init__(self, *args, **kwargs):
        """ Init user """
        super().__init__(*args, **kwargs)




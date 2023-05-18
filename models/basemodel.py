#!/usr/bin/env python3
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import models


# Base class from which all mapped classes should inherit
Base = declarative_base()
# Date format
date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Defining the base class
    """
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Init constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """
        Updates the instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """ Str representation """
        return "[{:s}] {}".format(self.__class__.__name__, self.__dict__)



    def to_dict(self, save_fs=None):
        """ Returns a dictionary containing all key/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(date)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(date)
        new_dict["_class__"] = self.__class__.__name__
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """
        Delete the current instance from the storage
        """
        models.storage.delete(self)

#!/usr/bin/env python3
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


# Base class from which all mapped classes should inherit
Base = declarative_base()
# Date format
date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Defining the base class
    """
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    status = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, **kwargs):
        """Init constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Updates the instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

        

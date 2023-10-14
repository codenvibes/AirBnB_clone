#!/usr/bin/python3
"""
This module defines the Amenity class, a subclass of BaseModel.

Auth: codenvibes & amoskarugo
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class represents an Amenity and inherits from BaseModel.

    Attributes:
    - name (str): The name of the Amenity.
    """
    name = ""

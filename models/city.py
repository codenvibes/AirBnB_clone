#!/usr/bin/python3
"""
This module defines the City class, which is a subclass of the BaseModel class.
It represents a city and its associated state_id and name.

Author: codenvibes & amoskarugo
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents a city and inherits from the BaseModel
    class.
    It includes attributes for state_id and name, as well as
    methods for creating, updating, and managing City objects.
    """
    state_id = ""
    name = ""

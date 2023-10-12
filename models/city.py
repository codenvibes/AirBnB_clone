#!/usr/bin/python3
"""
This module defines the City class, which is a subclass of the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class city that inherits from BaseModel
    """
    state_id = ""
    name = ""

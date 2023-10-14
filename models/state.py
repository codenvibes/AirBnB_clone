#!/usr/bin/python3
"""
This module defines the State class, which is a subclass of BaseModel.

Auth: codenvibes & amoskarugo
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class is a subclass of BaseModel and represents a state in
    your application.

    Attributes:
        name (str): The name of the state.
    """
    name = ""

#!/usr/bin/python3
"""
This module defines the User class, which is a subclass of BaseModel.
It represents user information such as email, password, first name,
and last name.

Authors: codenvibes, amoskarugo
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class representing user information, inherits from BaseModel.

    Attributes:
        - email (str): The user's email address.
        - password (str): The user's password.
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

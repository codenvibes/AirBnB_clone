#!/usr/bin/python3
"""
This module defines the Review class, a subclass of BaseModel.

Auth: codenvibes & amoskarugo
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review.

    This class inherits from the BaseModel class and is used to
    create and manage review objects.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

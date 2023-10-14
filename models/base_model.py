#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as a
foundation for other models in the application.
It provides common attributes and methods for initialization,
saving, and serialization to a dictionary.

Auth: codenvibes & amoskarugo
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models in the application.

    This class provides a foundation for other models by defining common
    attributes and methods such as initialization, saving, and serialization
    to a dictionary.

    Attributes:
        - id (str): A unique identifier for each instance.
        - created_at (datetime): The timestamp when the instance was created.
        - updated_at (datetime): The timestamp when the instance
        was last updated.

    Methods:
        - __init__: Initializes a new instance of the BaseModel class.
        - __str__: Returns a string representation of the instance.
        - save: Updates the 'updated_at' timestamp and saves the
        instance to storage.
        - to_dict: Converts the instance to a dictionary for serialization.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            - *args: Variable-length positional arguments (not used).
            - **kwargs: Variable-length keyword arguments, used for
            deserialization.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            - str: A string in the format "[ClassName] (id) attribute_dict".
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        Update the 'updated_at' timestamp and save the instance to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the instance to a dictionary for serialization.

        Returns:
            - dict: A dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

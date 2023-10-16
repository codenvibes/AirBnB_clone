#!/usr/bin/python3

"""Base model module that defines a class
    that serves as base of other classes
"""
import uuid
from datetime import time, datetime
import models


class BaseModel:
    """Base model class that defines all common attributes/methods
        for other classes.
    """

    def __init__(self, *args, **kwargs):

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)


    def __str__(self):
        """return string representation of baseclass instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """converts instance attributes into dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict


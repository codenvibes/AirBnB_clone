#!/usr/bin/python3
"""
This module provides a FileStorage class for storing and retrieving
objects in a JSON file.

Auth: codenvibes & amoskarugo
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    FileStorage class

    This class provides methods for storing, retrieving, and
    managing objects in a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: The object to be added.
        """
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """
        Save objects to a JSON file.
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Reload objects from a JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                object_dict = json.load(file)
                for value in object_dict.values():
                    class_name = value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

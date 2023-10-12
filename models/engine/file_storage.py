#!/usr/bin/python3

"""FileStorage module for serialization and deserialization"""

import json
from models.base_model import BaseModel

class FileStorage:
    """class FileStorage that serializes instances to a
     JSON file and deserializes JSON file to instances:
     """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """appends new object to the dictionary __objects

        Args:
            obj (object): object to be added

        """

        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

        objects_dict = {}

        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as file_storage:
            json.dump(objects_dict, file_storage, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn't exist,
         no exception should be raised)"""

        try:
            with open("file.json", "r") as file_storage:
                objects_dict = json.load(file_storage)
                for key, value in objects_dict.items():
                    class_name, id = key.split(".")
                    self.__objects[f"{key}"] = globals()[class_name](**value)
        except FileNotFoundError:
            pass

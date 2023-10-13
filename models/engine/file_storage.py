#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        object_dict = FileStorage.__objects
        serialized_objects = {key: object_dict[key].to_dict() for key in object_dict.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for value in objects_dict.values():
                    class_name = value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass


#!/usr/bin/python3
# Auth: codenvibes & amoskarugo

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, {
            'my_number': self.my_number,
            'name': self.name,
            'updated_at': self.updated_at,
            'id': self.id,
            'created_at': self.created_at
        }))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        key_order = ['my_number', 'name', '__class__', 'updated_at', 'id', 'created_at'] 
        ordered_dict = {key: obj_dict[key] for key in key_order}
        return ordered_dict

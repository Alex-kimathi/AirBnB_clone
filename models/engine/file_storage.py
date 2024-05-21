#!/usr/bin/python3
""" Contains FileStorage class"""
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """ serializes instances to a JSON file &
    deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj
        key <obj class name>.id """
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        save_dict = {}
        for key, value in FileStorage.__objects.items():
            save_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(save_dict))

    def reload(self):
        """ deserializes the JSON file to __objects """
        if not (os.path.exists(FileStorage.__file_path)):
            pass
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                reload_dict = json.load(f)

                for obj in reload_dict.values():
                    cname = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cname)(**obj))

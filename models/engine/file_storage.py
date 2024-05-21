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
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
        key <obj class name>.id """
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        save_dict = {}
        for key, value in self.__objects.items():
            save_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(save_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        cls_dict = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
            'User': User
        }
        if not (os.path.exists(FileStorage.__file_path)):
            pass
        else:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                reload_dict = json.load(f)

                for key, value in reload_dict.items():
                    cname = key.split(".")[0]
                    self.__objects[key] = cls_dict[cname](**value)

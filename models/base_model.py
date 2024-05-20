#!/usr/bin/python3
""" BaseModel Module """
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
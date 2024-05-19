import uuid
from datetime import datetime


class BaseModel:
    """
    Creates a base class where other classes will inherit
    when an instance of the class is called, the parameters are updated
    Assisgns a unique id, time created and time updated
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
            else:
                self.id = (uuid.uuid4)
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

    """converts the output of the instance to a string """

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    """Upated the time updated once the instance is saved """
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all the key or values on __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

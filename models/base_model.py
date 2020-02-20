#!/usr/bin/python3
'''Module that has the class Base Model
'''
import uuid
import datetime
import models


class BaseModel():
    '''Class that defines all common attibutes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''Construct method
        if kwargs is not empty, create a new object with its definitions
        else, create a new id a sets the actual date/time to the attibutes
        created and updated
        '''
        if kwargs is not None and kwargs.__len__() != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''String rbepresentation of the object
        '''
        rp = "[{:s}] ({:s}) {:s}"
        d = self.__dict__
        return rp.format(self.__class__.__name__, self.id, str(d))

    def save(self):
        '''Update the attribute of updated_at
        '''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary representation of the instance
        '''
        dict_rep = dict(self.__dict__)
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep

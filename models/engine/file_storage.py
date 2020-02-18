#!/usr/bin/python3
'''Module that has the FileStorage class
'''
import json
from models.base_model import BaseModel


class FileStorage():
    '''Class that serializes instances to a JSON file
    and deserializes JSON files to instances
    '''
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        '''Return the dictionary
        '''
        return self.__objects

    def new(self, obj):
        '''Sets a new object into __objects
        '''
        k = obj.__class__.__name__ + '.' + obj.id
        self.__objects[k] = obj

    def save(self):
        '''Serializes __objects to the JSON file at __file_path
        '''
        ser_d = dict()
        for k, v in self.__objects.items():
            ser_d[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as a_file:
            json.dump(ser_d, a_file)

    def reload(self):
        '''Deserializes the JSON file at __file_path to __objects
        '''

        try:
            with open(self.__file_path, mode='r', encoding="utf-8") as a_file:
                ser_d = json.load(a_file)
        except FileNotFoundError:
            ser_d = dict()

        if ser_d.__len__() != 0:
            from models.base_model import BaseModel
            for k, v in ser_d.items():
                value = eval(v["__class__"])(**v)
                self.__objects[k] = value

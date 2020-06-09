#!/usr/bin/python3
""" class base for start unit test """
import json


class Base(object):
    """Base class

    Args:
        object (int): id for the new object instance
    """

    __nb_objects = 0
    cosas = 0

    def __init__(self, id=None):
        """Inicialice var object

        Args:
            id (int): value for id object. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """gerenate JSON output

        Args:
            list_dictionaries (dict): dict to convert to json format

        Returns:
            str: json representation of list_dictionaries
        """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """funtion for safe to json file_name

        Args:
            list_objs (list): list of the object
        """

        file_name = cls.__name__ + '.json'
        with open(file_name, mode='w', encoding='utf-8') as myfile:
            if list_objs is None:
                myfile.write(Base.to_json_string(list_objs))
            else:
                l_dict = []
                for i in range(len(list_objs)):
                    l_dict.append(list_objs[i].to_dictionary())
                myfile.write(json.dumps(l_dict))

    @staticmethod
    def from_json_string(json_string):
        """convert json to python object

        Args:
            json_string (str): string to convert

        Returns:
            list: ret
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create objeto dummi

        Returns:
            objet: object is intance of call funtion create
        """

        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                new = cls(2, 10)
            else:
                new = cls(80)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """load file json format

        Returns:
            list: list of object create
        """

        file = cls.__name__ + '.json'
        with open(file, mode='r', encoding='utf-8') as myfile:
            if myfile is None:
                return("[]")
            else:
                new_list = cls.from_json_string(myfile.read())
                new_obj = []
                for obj in new_list:
                    new_obj.append(cls.create(**obj))
                return new_obj
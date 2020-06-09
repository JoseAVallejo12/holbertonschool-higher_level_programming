#!/usr/bin/python3
""" class base for start unit test """
import json
import csv


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
        """ convert json to python object

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
        """ create objeto dummi

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
        """
            load_from_file method:
            a method that returns a list of instances.
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if cls is None:
            return newlist
        try:
            with open(filename, mode="r", encoding='utf-8') as Myfile:
                newlist = cls.from_json_string(Myfile.read())
            for item in range(len(newlist)):
                newlist[item] = cls.create(**newlist[item])
        except Exception:
            pass
        return newlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes a object's list string representation
        into a CVS file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as file:
            string = csv.writer(file)
            if cls.__name__ is "Square":
                for i in list_objs:
                    string.writerow([i.id, i.size, i.x, i.y])
            elif cls.__name__ is "Rectangle":
                for i in list_objs:
                    string.writerow([i.id, i.width, i.height, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        reads from a CVS file an object's list
        string representation.
        """
        filename = cls.__name__ + ".csv"
        mylist = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                read = csv.reader(file)
                for i in read:
                    if cls.__name__ is "Square":
                        dict1 = {
                            "id": int(i[0]), "size": int(i[1]),
                            "x": int(i[2]), "y": int(i[3])
                        }
                    elif cls.__name__ is "Rectangle":
                        dict1 = {
                            "id": int(i[0]), "width": int(i[1]),
                            "height": int(i[2]), "x": int(i[3]),
                            "y": int(i[4])
                        }
                    mylist.append(cls.create(**dict1))
            return mylist
        except:
            return []

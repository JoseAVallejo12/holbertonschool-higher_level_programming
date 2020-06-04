#!/usr/bin/python3
""" define a new class student """


class Student(object):
    """Class Studen

    Args:
        object ([object]): class
    """

    def __init__(self, first_name, last_name, age):
        """inicialice var object

        Args:
            first_name ([str]): first name
            last_name ([str]): last name
            age ([int]): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Define a new dict

        Returns:
            [dict]: data en format dict
        """
        new_dict = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__

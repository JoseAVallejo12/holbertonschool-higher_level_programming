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

    def to_json(self):
        """Define a new dict

        Returns:
            [dict]: data en format dict
        """
        new_dict = {}
        new_dict.update(first_name=self.first_name)
        new_dict.update(last_name=self.last_name)
        new_dict.update(age=self.age)
        return new_dict

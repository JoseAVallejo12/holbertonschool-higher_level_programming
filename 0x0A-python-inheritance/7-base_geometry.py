#!/usr/bin/python3
""" define an empty class """


class BaseGeometry(object):
    """ new class """

    def area(self):
        """ funtion for calculate area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ funtion for validate integer object """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

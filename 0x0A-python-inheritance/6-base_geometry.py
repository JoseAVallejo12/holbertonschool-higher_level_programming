#!/usr/bin/python3
""" define an empty class """


class BaseGeometry(object):
    """ new class """

    def area(self):
        """ funtion for calculate area """
        raise Exception("area() is not implemented")

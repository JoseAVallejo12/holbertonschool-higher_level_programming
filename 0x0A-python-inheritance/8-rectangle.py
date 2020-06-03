#!/usr/bin/python3
""" create a new class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle inherits of besegeometry """

    def __init__(self, width, heigth):
        """ init method for private attribute """

        super().integer_validator('width', width)
        super().integer_validator('height', heigth)
        self.__width = width
        self.__heigth = heigth

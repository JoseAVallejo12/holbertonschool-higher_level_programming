#!/usr/bin/python3
""" create a new class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle inherits of besegeometry """

    def __init__(self, width, heigth):
        """
            Intialize a new Rectangle.
            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
        """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', heigth)
        self.__heigth = heigth

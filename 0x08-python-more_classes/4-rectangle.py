#!/usr/bin/python3
"""
    Jose vallejo <1545@holbertonschool.com
    class rectangle
    @width, @height must be integer number >= 0
"""


class Rectangle(object):
    """ class rectangle """

    def __init__(self, width=0, height=0):
        """ init for height and width """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Return integer value of area """
        return self.__width * self.__height

    def perimeter(self):
        """ return int value of perimeter """
        if self.__width or self.__height != 0:
            return ((self.__height + self.__width) * 2)
        else:
            return 0

    def __str__(self):
        """Returns a printable string"""

        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for i in range(self.__height):
            if i == self.__height - 1:
                string += self.__width * '#'
            else:
                string += self.__width * '#' + '\n'
        return string

    def __repr__(self):
        """Returns a representation of printable string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

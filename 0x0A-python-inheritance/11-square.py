#!/usr/bin/python3
""" create a new class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Scuare inherits of Rectagle """

    def __init__(self, size):
        """
            Intialize a new Scuare.
            Args:
                size (int): The width of the new Rectangle.
        """

        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ method auto thigger with print fun """

        return "[Square] {}/{}".format(self.__size, self.__size)

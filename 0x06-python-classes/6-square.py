#!/usr/bin/python3
# 6-square.py
# jose vallejo <1545@holbertonschool.com>
""" create a new class """


class Square(object):
    """ create Square class """

    def __init__(self, size=0, position=(0, 0)):
        """ inicialice size var """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter method for private size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for private size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getter method for private position """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter method for private position """
        if type(value) is not tuple or\
            len(value) != 2 or\
            type(value[0] and value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Method for Calculate area """
        return self.__size * self.__size

    def my_print(self):
        """ Method for print square # in stdout """
        if self.__size == 0:
            print()
            return
        else:
            x = self.__size
            y = self.__position[0]
            for i in range(self.__position[1]):
                print("")
            while self.__size != 0:
                print(y * " ", end="")
                print(x * "#")
                self.__size -= 1

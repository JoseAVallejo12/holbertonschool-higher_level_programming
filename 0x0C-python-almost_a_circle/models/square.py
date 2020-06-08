#!/usr/bin/python3
# jose vallejo contreras
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """constructor

        Args:
            size (int): side of square
            x (int, optional): axis x. Defaults to 0.
            y (int, optional): axis y. Defaults to 0.
            id (int, optional): description. Defaults to None.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size var

        Returns:
            int: value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for size """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __str__(self):
        """overloading

        Returns:
            str: string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )

#!/usr/bin/python3
""" create a new class Scuare """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ new class
        Args:
            Rectangle (class): Inheritance: from Base Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor
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
        """
        This function returns the size (width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            This function sets the size (width and height)
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ overloading

            Returns:
                str: string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """ Method for assig argv to var class """
        ln = len(args)
        if not args:
            if kwargs.get('id') is not None:
                self.id = kwargs.get('id')
            if kwargs.get('size') is not None:
                self.size = kwargs.get('size')
            if kwargs.get('x') is not None:
                self.x = kwargs.get('x')
            if kwargs.get('y') is not None:
                self.y = kwargs.get('y')
        else:
            if ln >= 1 and args[0] is not None:
                self.id = args[0]
            if ln >= 2 and args[1] is not None:
                self.size = args[1]
            if ln >= 3 and args[2] is not None:
                self.x = args[2]
            if ln >= 4 and args[3] is not None:
                self.y = args[3]

    def to_dictionary(self):
        """ diccionari method

            Returns:
                dict: dictionari of values
        """

        new_dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return new_dict

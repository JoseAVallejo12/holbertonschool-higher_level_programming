#!/usr/bin/python3
""" class base for start unit test """


class Base(object):
    """Base class

    Args:
        object (int): id for the new object instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Inicialice var object

        Args:
            id (int): value for id object. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

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

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading

        Returns:
            str: string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

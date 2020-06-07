#!/usr/bin/python3
""" create a new class Rectangle """
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor

        Args:
            width (int): ancho
            height (int): alto value
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id (int, optional): identify for object. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ method getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area funtion

        Returns:
            int: area cal
        """
        return self.__width * self.__height

    def display(self):
        """ print rentangle with # char """
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """str method for print string defined

        Returns:
            [str]: print defined string in stdout
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x,
            self.__y, self.__width,
            self.__height
        )

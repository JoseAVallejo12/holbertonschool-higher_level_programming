#!/usr/bin/python3
""" unit test for Rectangle.py file """
import unittest

# Rectangle = __import__('base.py').Rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestTask_Two(unittest.TestCase):
    """
        unit testing class Rectangle
    """

    def test_a01_id(self):
        """ check count and assignation of id in empty argvs """
        self.assertEqual(Rectangle(5, 5, 0, 0, 1).id, 1)
        self.assertTrue(Rectangle(5, 5, 0, 0).id == 1)
        self.assertTrue(Rectangle(5, 5, 0, 0).id == 2)
        self.assertEqual(Rectangle(5, 5, 0, 0, "holberton").id, "holberton")

    def test_a02_instance(self):
        """ check inherence and subclass """
        x = Rectangle(5, 5, 0, 0)
        self.assertTrue(
            type(x) is Rectangle and issubclass(type(x), Rectangle))

    def test_a03_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)
            
    def test_a04_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_a05_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_a06_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_a07_setter_getter(self):
        gt = Rectangle(5, 7, 3, 8, 20)
        self.assertEqual(gt.width, 5)
        self.assertEqual(gt.height, 7)
        self.assertEqual(gt.x, 3)
        self.assertEqual(gt.y, 8)
        self.assertEqual(gt.id, 20)




class TestTask_Three(unittest.TestCase):

    def test_a03_TypeError_width(self):
        """ Checks for task 3. Validate attributes """

        """ check TypeError for witdh, height, x and y """
        with self.assertRaises(TypeError):
            Rectangle('q', (1, 3), 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle([1, 5], 'u', 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle("hola", {'v': 1, 'c': 3}, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle("hola", None, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(None)



    def test_a04_ValueError(self):
        """ check ValueError for witdh, height, x and y """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 0, 0)

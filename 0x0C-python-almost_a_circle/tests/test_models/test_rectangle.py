#!/usr/bin/python3
""" unit test for Rectangle.py file """
import unittest

# Rectangle = __import__('base.py').Rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestTask_Two(unittest.TestCase):
    """ unit testing class Rectangle task 2. First Rectangle """

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
            type(x) is Rectangle and issubclass(type(x), Base))

    def test_a03_private_width(self):
        """ validate private attribute for __witdth """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_a04_private_height(self):
        """ validate private attribute for __height """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_a05_private_x(self):
        """ validate private attribute for _x """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_a06_private_y(self):
        """ validate private attribute for _y """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_a07_getter(self):
        """ test getters and setters method """
        gt = Rectangle(5, 7, 3, 8, 20)
        self.assertEqual(gt.width, 5)
        self.assertEqual(gt.height, 7)
        self.assertEqual(gt.x, 3)
        self.assertEqual(gt.y, 8)
        self.assertEqual(gt.id, 20)

    def test_a08_setters(self):
        gt = Rectangle(4, 5, 8, 1, 20)
        gt.width = 30
        self.assertEqual(gt.width, 30)
        gt.height = 33
        self.assertEqual(gt.height, 33)
        gt.x = 56
        self.assertEqual(gt.x, 56)
        gt.y = 14
        self.assertEqual(gt.y, 14)


class TestTask_Three(unittest.TestCase):
    """ unit testing class Rectangle task 3. Validate attributes """

    def test_a09_TypeError_width(self):
        """ check TypeError for witdh """
        with self.assertRaises(TypeError):
            Rectangle('q', 6, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle([1, 5], 6, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle("hola", 6, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle({'1': 2, 'v': "hola"}, 6, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(None, 5, 0, 0, 0)

    def test_a10_TypeError_height(self):
        """ check ValueError for height """
        with self.assertRaises(TypeError):
            Rectangle(6, 'j', 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(4, [1, 5], 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(5, "hola", 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(2, {'1': 2, 'v': "hola"}, 0, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(5, None, 0, 0, 0)

    def test_a11_TypeError_x(self):
        """ check ValueError for x """
        with self.assertRaises(TypeError):
            Rectangle(6, 6, 'x', 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(4, 4, [1, 5], 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(5, 5, "hola", 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(2, 3, {'1': 2, 'v': "hola"}, 0, 0)

        with self.assertRaises(TypeError):
            Rectangle(5, 5, None, 0, 0)

    def test_a11_TypeError_y(self):
        """ check ValueError for x """
        with self.assertRaises(TypeError):
            Rectangle(6, 6, 2, 'y', 0)

        with self.assertRaises(TypeError):
            Rectangle(4, 4, 3, [1, 5], 0)

        with self.assertRaises(TypeError):
            Rectangle(5, 5, 6, "hola", 0)

        with self.assertRaises(TypeError):
            Rectangle(2, 3, 3, {'1': 2, 'v': "hola"}, 0)

        with self.assertRaises(TypeError):
            Rectangle(5, 5, 4, None, 0)

    def test_a12_ValueError_width(self):
        """ check ValueError for width """
        with self.assertRaises(ValueError):
            Rectangle(-5, 5, 0, 0, 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 5, 0, 0, 1)

    def test_a13_ValueError_height(self):
        """ check ValueError for height """
        with self.assertRaises(ValueError):
            Rectangle(5, -5, 0, 0, 1)

        with self.assertRaises(ValueError):
            Rectangle(5, 0, 0, 0, 1)

    def test_a13_ValueError_x(self):
        """ check ValueError for x """
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1, 0, 1)

    def test_a13_ValueError_y(self):
        """ check ValueError for x """
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 4, -2, 1)


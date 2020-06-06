#!/usr/bin/python3
""" unit test for max_integer function """
import unittest

# Rectangle = __import__('base.py').Rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestClassRectangle(unittest.TestCase):
    """
        unit testing class Rectangle
    """

    def test_a001(self):
        """ Checks for task 2. First Rectangle """

        a = Rectangle(5, 5, 0, 0, 1)

        """ check id object """
        self.assertEqual(a.id, 1)

        """ check inherence and subclass """
        self.assertTrue(type(a) is Rectangle and issubclass(type(a), Rectangle))

        """ check count and assignation of id in empty argvs """
        b1 = Rectangle(5, 5, 0, 0)
        b2 = Rectangle(5, 5, 0, 0)
        b3 = Rectangle(5, 5, 0, 0, "holberton")
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 2)
        self.assertEqual(b3.id, "holberton")

    def test_a002(self):
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

        """ check ValueError for witdh, height, x and y """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 0, 0)
            
'''

    def test_a003(self):
        pass


    def test_a004(self):
        pass
'''
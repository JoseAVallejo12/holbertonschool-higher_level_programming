""" unit test for max_integer function """

import unittest

#Base = __import__('base.py').Base
from models.base import Base


class TestClassBase(unittest.TestCase):
    """
        unit testing class
    """

    def test_a001(self):
        """ check empty argument send to function """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(None)
        self.assertEqual(b4.id, 4)

    def test_a002(self):
        """ check with argument send to function"""
        b5 = Base(13)
        self.assertEqual(b5.id, 13)
        b6 = Base('s')
        self.assertEqual(b6.id, 's')
        b7 = Base("holberton")
        self.assertEqual(b7.id, "holberton")

    def test_a003(self):
        """ check send more of one argument to funtion """
        with self.assertRaises(TypeError):
            Base(5, 4)
        with self.assertRaises(TypeError):
            Base([1, 3], [3, 5])

    def test_a004(self):
        """ check if value id not is increced after error """
        b8 = Base()
        self.assertEqual(b8.id, 5)

#!/usr/bin/python3
""" unit test for max_integer function """
import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """
        unit testing class
    """

    def test_a001(self):
        """ check empty argument send to function """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(None).id, 4)

    def test_a002(self):
        """ check with argument send to function"""
        self.assertEqual(Base(13).id, 13)
        self.assertEqual(Base('s').id, 's')
        self.assertEqual(Base("holberton").id, "holberton")

    def test_a003(self):
        """ check send more of one argument to funtion """
        with self.assertRaises(TypeError):
            Base(5, 4)
        with self.assertRaises(TypeError):
            Base([1, 3], [3, 5])

    def test_a004(self):
        """ check if value id not is increced after error """
        self.assertEqual(Base().id, 5)

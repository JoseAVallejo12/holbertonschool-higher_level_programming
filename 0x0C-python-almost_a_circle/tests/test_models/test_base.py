#!/usr/bin/python3
""" unit test for file base.py """
import unittest
from models.base import Base


class TestTask_One(unittest.TestCase):
    """ unit testing class Base task 1. Base class """

    def test_a01(self):
        """ check empty argument send to function """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(None).id, 4)

    def test_a02(self):
        """ check with argument send to function"""
        self.assertEqual(Base(13).id, 13)
        self.assertEqual(Base('s').id, 's')
        self.assertEqual(Base("holberton").id, "holberton")

    def test_a03(self):
        """ check send more of one argument to funtion """
        with self.assertRaises(TypeError):
            Base(5, 4)
        with self.assertRaises(TypeError):
            Base([1, 3], [3, 5])

    def test_a04(self):
        """ check if value id not is increced after error """
        self.assertEqual(Base().id, 5)

    def test_a05_private(self):
        """ validate private attribute for __nb_objects """
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

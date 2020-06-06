#!/usr/bin/python3
""" unit test for Rectangle.py file """
import unittest
import io, contextlib
# Rectangle = __import__('base.py').Rectangle
from models.rectangle import Rectangle
from models.base import Base


class TestTask_Two(unittest.TestCase):
    """ unit testing class Rectangle task 2. First Rectangle """

    def test_aa1_id(self):
        """ check count and assignation of id in empty argvs """
        self.assertEqual(Rectangle(5, 5, 0, 0, 1).id, 1)
        self.assertEqual(Rectangle(5, 5, 0, 0).id, 3)
        self.assertEqual(Rectangle(5, 5, 0, 0).id, 4)
        self.assertEqual(Rectangle(5, 5, 0, 0, "holberton").id, "holberton")

    def test_aa2_instance(self):
        """ check inherence and subclass """
        x = Rectangle(5, 5, 0, 0)
        self.assertTrue(
            type(x) is Rectangle and issubclass(type(x), Base))

    def test_aa3_private_width(self):
        """ validate private attribute for __witdth """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_aa4_private_height(self):
        """ validate private attribute for __height """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_aa5_private_x(self):
        """ validate private attribute for _x """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_aa6_private_y(self):
        """ validate private attribute for _y """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_aa7_getter(self):
        """ test getters and setters method """
        gt = Rectangle(5, 7, 3, 8, 20)
        self.assertEqual(gt.width, 5)
        self.assertEqual(gt.height, 7)
        self.assertEqual(gt.x, 3)
        self.assertEqual(gt.y, 8)
        self.assertEqual(gt.id, 20)

    def test_aa8_setters(self):
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

    def test_ab1_TypeError_width(self):
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

        with self.assertRaises(TypeError):
            Rectangle(True, 3, 0, 0, 0)

    def test_ab2_TypeError_height(self):
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

        with self.assertRaises(TypeError):
            Rectangle(3, True, 0, 0, 0)

    def test_ab3_TypeError_x(self):
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

        with self.assertRaises(TypeError):
            Rectangle(3, 4, True, 0, 0)

    def test_ab4_TypeError_y(self):
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

        with self.assertRaises(TypeError):
            Rectangle(3, 4, 5, True, 0)

    def test_ab5_ValueError_width(self):
        """ check ValueError for width """
        with self.assertRaises(ValueError):
            Rectangle(-5, 5, 0, 0, 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 5, 0, 0, 1)

    def test_ab6_ValueError_height(self):
        """ check ValueError for height """
        with self.assertRaises(ValueError):
            Rectangle(5, -5, 0, 0, 1)

        with self.assertRaises(ValueError):
            Rectangle(5, 0, 0, 0, 1)

    def test_ab7_ValueError_x(self):
        """ check ValueError for x """
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1, 0, 1)

    def test_ab8_ValueError_y(self):
        """ check ValueError for x """
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 4, -2, 1)


class TestTask_Four(unittest.TestCase):
    """ unit testing class Rectangle task 4. Area first """

    def test_ac1_area1(self):
        """ check value resul 4x5 = 20 """
        c = Rectangle(4, 5)
        self.assertEqual(c.area(), 20)

    def test_ac2_area2(self):
        """ check value resul 4x5 = 20 """
        c = Rectangle(8, 5)
        self.assertEqual(c.area(), 40)

class TestTask_five(unittest.TestCase):
    """ unit testing class Rectangle task 5. Display #0 """

    def test_ad0_display1(self):
        """This function tests the display function"""
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "##\n##\n##\n")

    def test_ad1_display2(self):
        """This function tests the display function"""
        r1 = Rectangle(5, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n")
#!/usr/bin/python3
""" unit test for Rectangle.py file """
import unittest
from io import StringIO
import sys
import contextlib
import pep8
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """ unittesting class Rectangle task:
        10. And now, the Square!, 11. Square size """

    def test_pep8_model(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_00_documentation(self):
        """Test to see if documentation is created and correct"""
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertTrue(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertTrue(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)

    def test_aa_instance(self):
        """ check inherence and subclass """
        x = Square(5)
        self.assertTrue(
            type(x) is Square and issubclass(type(x), Rectangle))

    def test_aa_private_size(self):
        """ validate private attribute for __size """
        with self.assertRaises(AttributeError):
            print(Square(5).__width)

    def test_aa_getter(self):
        """ test getters and setters method """
        gt = Square(2, 5)
        self.assertEqual(gt.size, 2)

    def test_aa_setters(self):
        """ test setters and setters method """
        gt = Square(4, 5)
        gt.width = 30
        self.assertEqual(gt.width, 30)

    def test_aa_str(self):
        """ test 1 """
        r1 = Square(2, 2, 2, 2)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (2) 2/2 - 2\n")

    def test_aa_display1(self):
        """This function tests the display function"""
        r1 = Square(3)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "###\n###\n###\n")

    def test_aa_display2(self):
        """This function tests the display function"""
        r1 = Square(3, 1, 3)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")

    def test_aa_error(self):
        """ handle error """
        strs1 = "takes from 2 to 5 positional arguments but 6 were"
        strs2 = "missing 1 required positional argument: 'size'"
        with self.assertRaisesRegex(TypeError, strs1):
            Square(22, 3, 4, 3, 5)
        with self.assertRaisesRegex(TypeError, strs2):
            Square()

    def test_ab_args(self):
        """ testing positional arguments """
        r1 = Square(50)
        self.assertEqual(r1.size, 50)
        r1.update(10, 22, 14, 5)
        self.assertEqual(r1.size, 22)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (10) 14/5 - 22\n")

    def test_ab_kwargs(self):
        """ testing positional arguments """
        r1 = Square(50)
        self.assertEqual(r1.size, 50)
        r1.update(y=5, id=10, x=14, size=22)
        self.assertEqual(r1.size, 22)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (10) 14/5 - 22\n")

    def test_ac_load_dict(self):
        """ testing positional arguments """
        new_dict = {'x': 14, 'y': 5, 'id': 10, 'size': 22}
        r1 = Square(50)
        self.assertEqual(r1.size, 50)
        r1.update(**new_dict)
        self.assertEqual(r1.size, 22)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Square] (10) 14/5 - 22\n")

    def test_ac_type_dict(self):
        """ testing positional arguments """
        new_dict = {'x': 14, 'y': 5, 'id': 10, 'size': 22}
        r1 = Square(50)
        r1.update(**new_dict)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(type(r1.to_dictionary()))
        self.assertEqual(f.getvalue(), "<class 'dict'>\n")

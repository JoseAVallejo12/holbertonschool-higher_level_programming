#!/usr/bin/python3
""" unit test for Rectangle.py file """
import unittest
from io import StringIO
import sys
import contextlib
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ testing pep8 style and __document__ """

    def test_pep8_model(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """Test to see if documentation is created and correct"""
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)

    def test_aa_id(self):
        """ check count and assignation of id in empty argvs """
        Base._Base__nb_objects = 0
        self.assertEqual(Rectangle(5, 5, 0, 0, 1).id, 1)
        self.assertEqual(Rectangle(5, 5, 0, 0).id, 1)
        self.assertEqual(Rectangle(5, 5, 0, 0).id, 2)
        self.assertEqual(Rectangle(5, 5, 0, 0, "holberton").id, "holberton")

    def test_aa_instance(self):
        """ check inherence and subclass """
        x = Rectangle(5, 5, 0, 0)
        self.assertTrue(
            type(x) is Rectangle and issubclass(type(x), Base))

    def test_aa_private_width(self):
        """ validate private attribute for __witdth """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_aa_private_height(self):
        """ validate private attribute for __height """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_aa_private_x(self):
        """ validate private attribute for _x """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_aa_private_y(self):
        """ validate private attribute for _y """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_aa_getter(self):
        """ test getters and setters method """
        gt = Rectangle(5, 7, 3, 8, 20)
        self.assertEqual(gt.width, 5)
        self.assertEqual(gt.height, 7)
        self.assertEqual(gt.x, 3)
        self.assertEqual(gt.y, 8)
        self.assertEqual(gt.id, 20)

    def test_aa_setters(self):
        gt = Rectangle(4, 5, 8, 1, 20)
        gt.width = 30
        self.assertEqual(gt.width, 30)
        gt.height = 33
        self.assertEqual(gt.height, 33)
        gt.x = 56
        self.assertEqual(gt.x, 56)
        gt.y = 14
        self.assertEqual(gt.y, 14)

    def test_ab_TypeError_width(self):
        """ check TypeError for witdh """
        Base._Base__nb_objects = 0
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

    def test_ab_TypeError_height(self):
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

    def test_ab_TypeError_x(self):
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

    def test_ab_TypeError_y(self):
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

    def test_ab_ValueError_width(self):
        """ check ValueError for width """
        with self.assertRaises(ValueError):
            Rectangle(-5, 5, 0, 0, 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 5, 0, 0, 1)

    def test_ab_ValueError_height(self):
        """ check ValueError for height """
        with self.assertRaises(ValueError):
            Rectangle(5, -5, 0, 0, 1)

        with self.assertRaises(ValueError):
            Rectangle(5, 0, 0, 0, 1)

    def test_ab_ValueError_x(self):
        """ check ValueError for x """
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1, 0, 1)

    def test_ab_ValueError_y(self):
        """ check ValueError for x """
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 4, -2, 1)

    def test_ac_area1(self):
        """ check value resul 4x5 = 20 """
        c = Rectangle(4, 5)
        self.assertEqual(c.area(), 20)

    def test_ac_area2(self):
        """ check value resul 4x5 = 20 """
        c = Rectangle(8, 5)
        self.assertEqual(c.area(), 40)

    def test_ad_display1(self):
        """This function tests the display function"""
        r1 = Rectangle(2, 3, 2, 1)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n  ##\n  ##\n  ##\n")

    def test_ad_display2(self):
        """This function tests the display function"""
        r1 = Rectangle(5, 3, 2, 2)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n  #####\n  #####\n  #####\n")

    def test_ad_display3(self):
        """This function tests the display function"""
        r1 = Rectangle(5, 3)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n")

    def test_ae_str(self):
        """ test 1 """

        r1 = Rectangle(4, 6, 2, 1, 12)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_ae_strs(self):
        """ test 2 """
        Base._Base__nb_objects = 0
        r1 = Rectangle(5, 5, 1)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

    def test_af_update(self):
        """ test stdout posicionated value (*args) """

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.update(89)
            print(r1)
            self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

    def test_af_updatee(self):
        """ test std out and set posicionated value (*args) """

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        with contextlib.redirect_stdout(f):
            print(r1)
            self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

    def test_af_updat(self):
        """ test std out and set posicionated value (*args) """

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        r1.update(56, 22, 33)
        self.assertEqual(r1.id, 56)
        self.assertEqual(r1.width, 22)
        self.assertEqual(r1.height, 33)
        with contextlib.redirect_stdout(f):
            print(r1)
            self.assertEqual(
                f.getvalue(), "[Rectangle] (56) 10/10 - 22/33\n")

    def test_af_updateee(self):
        """ test std out and set posicionated value (*args) """

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        r1.update(8, 23, 13, 88, 23)
        self.assertEqual(r1.id, 8)
        self.assertEqual(r1.width, 23)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 88)
        self.assertEqual(r1.y, 23)
        with contextlib.redirect_stdout(f):
            print(r1)
            self.assertEqual(f.getvalue(), "[Rectangle] (8) 88/23 - 23/13\n")

    def test_ag_update_a(self):
        """ test stdout """

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            r1.update(id=89)
            print(r1)
            self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

    def test_ag_updat_b(self):
        """ test std out and set nemed value (**kwargs) """

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        r1.update(width=2, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        with contextlib.redirect_stdout(f):
            print(r1)
            self.assertEqual(f.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

    def test_ag_update_c(self):
        """ test std out and set named value (**kwargs)"""

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        r1.update(id=56, height=33, width=22)
        self.assertEqual(r1.id, 56)
        self.assertEqual(r1.width, 22)
        self.assertEqual(r1.height, 33)
        with contextlib.redirect_stdout(f):
            print(r1)
            self.assertEqual(
                f.getvalue(), "[Rectangle] (56) 10/10 - 22/33\n")

    def test_ag_update_d(self):
        """ test std out and set named value (**kwargs)"""

        r1 = Rectangle(10, 10, 10, 10, 2)
        f = StringIO()
        r1.update(id=8, x=88, width=23, y=23, height=13)
        self.assertEqual(r1.id, 8)
        self.assertEqual(r1.width, 23)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 88)
        self.assertEqual(r1.y, 23)
        with contextlib.redirect_stdout(f):
            print(r1)
            self.assertEqual(f.getvalue(), "[Rectangle] (8) 88/23 - 23/13\n")

    def test_ac_load_dict(self):
        """ testing positional arguments """
        new_dict = {'x': 14, 'y': 5, 'id': 10, 'width': 22, 'height': 25}
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 9)
        r1.update(**new_dict)
        self.assertEqual(r1.width, 22)
        self.assertEqual(r1.height, 25)
        self.assertEqual(r1.x, 14)
        self.assertEqual(r1.y, 5)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(r1)
        self.assertEqual(f.getvalue(), "[Rectangle] (10) 14/5 - 22/25\n")

    def test_ac_type_dict(self):
        """ testing positional arguments """
        new_dict = {'x': 14, 'y': 5, 'id': 10, 'width': 22, 'height': 25}
        r1 = Rectangle(10, 2, 1, 9)
        r1.update(**new_dict)
        f = StringIO()
        with contextlib.redirect_stdout(f):
            print(type(r1.to_dictionary()))
        self.assertEqual(f.getvalue(), "<class 'dict'>\n")

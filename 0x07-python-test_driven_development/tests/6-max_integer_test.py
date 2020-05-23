""" unit test for max_integer function """

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaximumInteger(unittest.TestCase):
    """
        unit testing class
    """

    def test_with_no_input(self):
        self.assertEqual(max_integer(), None)

    def test_valid_input(self):
        lst = [1, 2, 3, 50]
        self.assertEqual(max_integer(lst), 50)

    def test_float(self):
        lst = [1.2, 2.3, 3.4, 50.8]
        self.assertEqual(max_integer(lst), 50.8)

    def test_mixed_integers(self):
        lst = [-1, -2, 3, -50]
        self.assertEqual(max_integer(lst), 3)

    def test_tuple_data(self):
        lst = (-1, -2, 3, -50)
        self.assertEqual(max_integer(lst), 3)

    def test_non_valid_list(self):
        new_list = ['hello', 0, 0, 0]
        with self.assertRaises(TypeError):
            max_integer(new_list)

#!/usr/bin/python3

import unittest

# from Prog1 import add
from prog2 import even

# class TestSum(unittest.TestCase):
#     def test_add(self):
#         """
#         Test case to add two numbers
#         """
#         x=5
#         y=10
#         result = add(x,y)
#         self.assertEqual(result, 15)
class Test_even(unittest.TestCase):
#         """
#         Test case to check if the number is even.
#         """
        def test_even(self):
                x=2
                result = even(x)
                self.assertEqual(result,1)
        def test_1(self):
                x=3
                result = even(x)
                self.assertEqual(result,1)
        def test_2(self):
                x=4
                result = even(x)
                self.assertEqual(result,1)
        def test_3(self):
                x=15
                result = even(x)
                self.assertEqual(result,1)
        def test_4(self):
                x=23
                result = even(x)
                self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import add
from prog2 import even

class TestSum(unittest.TestCase):
    def test_add(self):
        """
        Test case to add two numbers
        """
        x=5
        y=10
        result = add(x,y)
        self.assertEqual(result, 15)

    def test_even(self):
        """
        Test case to add two numbers
        """
        x=10
        result = even(x)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()

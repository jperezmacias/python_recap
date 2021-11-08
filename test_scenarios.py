import unittest
from several_functions import *

class NameTestCase(unittest.TestCase):

    def test_sum(self):
        result = getSum(5,10)
        self.assertEqual(result, 15)


    def test_outside_range(self):
        result = getSum(0,1)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
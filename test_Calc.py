import unittest
import Calc


class testCalc(unittest.TestCase):
    def test_sum(self):
        result = Calc.sum(3, 7)
        self.assertEqual(10, result)

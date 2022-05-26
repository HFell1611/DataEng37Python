from simple_calc import SimpleCalc
from unittest import TestCase


class CalcTest(TestCase):
    calc = SimpleCalc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertAlmostEqual(actual, expected, 3)

    def test_subtract(self):
        actual = self.calc.subtract(4, 2)
        expected = 2
        self.assertAlmostEqual(actual, expected, 5)

    def test_multiply(self):
        actual = self.calc.multiply(4, 2)
        expected = 8
        self.assertEqual(actual, expected)

    def test_divide(self):
        actual = self.calc.divide(4, 2)
        expected = 2
        self.assertEqual(actual, expected)

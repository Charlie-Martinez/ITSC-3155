import unittest
from .calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3, 2), 5)
        self.assertEqual(Calculator.add(-1, 2), 1)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 2), 1)
        self.assertEqual(Calculator.subtract(-1, 2), -3)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 2), 6)
        self.assertEqual(Calculator.multiply(-1, 2), -2)

    def test_divide(self):
        self.assertEqual(Calculator.divide(3, 2), 1.5)
        self.assertEqual(Calculator.divide(-1, 2), -0.5)


if __name__ == '__main__':
    unittest.main()
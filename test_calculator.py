# test_calculator.py

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 3), 9)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        self.assertEqual(calculator.divide(10, 0), "Error: Division by zero")

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_modulo(self):
        self.assertEqual(calculator.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(3, 5), 8)
        self.assertEqual(calculator.addition(-4, 2), -2)
        self.assertEqual(calculator.addition(1.7, 6.6), 8.30)
        self.assertEqual(calculator.addition("2.2", "3.1"), -1)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(9, 2), 7)
        self.assertEqual(calculator.subtraction(-4, 6), -10)
        self.assertEqual(calculator.subtraction(4.7, 1.9), 2.80)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(3, 4), 12)
        self.assertEqual(calculator.multiplication(-9, 3), -27)
        self.assertEqual(calculator.multiplication(2.4, 1.3), 3.12)

    def test_division(self):
        self.assertEqual(calculator.division(8, 4), 2)
        self.assertEqual(calculator.division(-9, 0), -1)
        self.assertEqual(calculator.division(4.8, 1.1), 4.36)

if __name__ == '__main__':
    unittest.main(verbosity=2)